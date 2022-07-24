import ccxt
import config

coinbase = ccxt.coinbasepro()
coinbase.apiKey = config.CB_PRO_API_KEY
coinbase.secret = config.CB_PRO_API_SECRET
coinbase.password = config.CB_PRO_PASSPHRASE

def order(side, quantity, symbol, price):
    if side == "BUY":
        try:
            print(f"Sending Order LIMIT - {side} {quantity} {symbol} @ ${price}")
            coinbase.create_limit_buy_order(symbol=symbol, amount=quantity, price=price, params={'stop_price': price})
            
        except Exception as e:
            print("an exception occured - {}".format(e))
            return False
        
        return order

    elif side == "SELL":
        try:
            print(f"Sending Order LIMIT - {side} {quantity} {symbol} @ ${price}")
            coinbase.create_limit_sell_order(symbol=symbol, amount=quantity, price=price, params={'stop_price':  price})
            
        except Exception as e:
            print("an exception occured - {}".format(e))
            return False
        
        return order