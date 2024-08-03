import websocket
import json
import os

api_key = os.getenv('FINNHUB_API_KEY')

# List of symbols to subscribe to
symbols = ['BINANCE:BTCUSDT', 'BINANCE:ETHUSDT', 'BINANCE:LTCUSDT']

def on_message(ws, message):
    print(f"Received message: {message}")

def on_error(ws, error):
    print(f"Error: {error}")

def on_close(ws, close_status_code, close_msg):
    print("### closed ###")

def on_open(ws):
    print("Opened connection")
    for symbol in symbols:
        subscribe_message = json.dumps({
            'type': 'subscribe',
            'symbol': symbol,
            'token': api_key
        })
        ws.send(subscribe_message)

if __name__ == "__main__":
    #websocket.enableTrace(True)
    ws = websocket.WebSocketApp(
        "wss://ws.finnhub.io?token=" + api_key,
        on_open=on_open,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close
    )
    ws.run_forever()
