import logging
from binance.client import Client
from binance.enums import *
from dotenv import load_dotenv
import os

class BasicBot:
    def __init__(self):
        load_dotenv()
        api_key = os.getenv("BINANCE_API_KEY")
        api_secret = os.getenv("BINANCE_API_SECRET")

        self.client = Client(api_key, api_secret)
        self.client.FUTURES_URL = "https://testnet.binancefuture.com"
        self.client.API_URL = "https://testnet.binancefuture.com"

    def place_market_order(self, symbol, side, quantity):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side.upper(),
                type=ORDER_TYPE_MARKET,
                quantity=quantity
            )
            logging.info(f"✅ Market order placed: {order}")
            return order
        except Exception as e:
            logging.error(f"❌ Error placing market order: {e}")
            return None

    def place_limit_order(self, symbol, side, quantity, price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side.upper(),
                type=ORDER_TYPE_LIMIT,
                timeInForce=TIME_IN_FORCE_GTC,
                quantity=quantity,
                price=price
            )
            logging.info(f"✅ Limit order placed: {order}")
            return order
        except Exception as e:
            logging.error(f"❌ Error placing limit order: {e}")
            return None

    def place_stop_limit_order(self, symbol, side, quantity, stop_price, limit_price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side.upper(),
                type=ORDER_TYPE_STOP,
                timeInForce=TIME_IN_FORCE_GTC,
                quantity=quantity,
                price=limit_price,
                stopPrice=stop_price
            )
            logging.info(f"✅ Stop-limit order placed: {order}")
            return order
        except Exception as e:
            logging.error(f"❌ Error placing stop-limit order: {e}")
            return None
