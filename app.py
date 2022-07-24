import json, config
from create_order import order
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    side = db.Column(db.String(6))
    quantity = db.Column(db.Integer)
    symbol = db.Column(db.String(10))
    price = db.Column(db.Float)
    order_num = db.Column(db.Integer)

    def __repr__(self):
        return f'<Order: {self.id}>'

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/webhook/', methods=['POST'])
def webhook():
    data = json.loads(request.data)

    side = data['strategy']['order_action'].upper()
    qty = data['strategy']['order_contracts']
    sym = data['ticker']
    price = data['strategy']['order_price']
    id = data['strategy']['order_id']

    if data['passphrase'] != config.WEBHOOK_PASSPHRASE:
        return {
            "code": "Error",
            "message": "Nice try, invalid passphrase"
        }
    elif data['passphrase'] == config.WEBHOOK_PASSPHRASE:
        order_response = order(side, qty, sym, price)

        if order_response:
            new_order = Orders(side=side, quantity=qty, symbol=sym, price=price,order_num=id)

            db.session.add(new_order)
            db.session.commit()

            return {
                "code": "Success",
                "message": "Order Processed"
                    }
        else:
            return {
                "code": "Error",
                "message": "Order Failed"
                    }

@app.route('/api/')
def endpoint():
    order_list = Orders.query.all()
    orders = []

    for order in order_list:
        orders.append({'order_id' : order.order_num,'Side' : order.side,'Quantity':order.quantity,'Symbol' : order.symbol,'Price' : order.price})

    return jsonify(orders)
