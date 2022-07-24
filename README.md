# trade-bot-tv-webhook
This trading bot recieves signal indicators from Trading View via webhook and creates an order within your coinbase pro account
The app also routes the confirmed trades to an API endpoint (@routes = '/api/') in the form of a json array

Prerequisite:

setup the indicator signal in your trading view account
add an alert and in the message field, paste the data from the webhook_payload.txt

get acount api info from coinbase pro. must have key, secret, and password

App Installation:

initiate the virtual env and pip install the requirements.txt
update the config.py file to include your personal coinbase pro account information (api key, secret, and password)
instantiate the database in the terminal:
        python> from app import db, Orders> db.create_all()

setup the flask env and app:
        $env:FLASK_ENV = "development"
        $env:FLASK_APP = "app"

start the flask server within the terminal by typing "flask run"
This app was deployed through heroku and already has the procfile/required installations
for deployment on another server, please update the requirements

Testing:

copy and paste webhook payload into a postman workspace (https://www.postman.com) and send it to your localhost url followed by "/webhook/" (ex: http://127.0.0.1:5000/webhook/)
if the webhook was sent successfully and the order was made, you will recieve a confirmation message back:
        {"code": "Success", "message": "Order Processed"}

if you do not recieve this message, check the terminal in your IDE for the failure reason.


