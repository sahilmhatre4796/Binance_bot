import logging
from bot import BasicBot

def get_user_input():
    symbol = input("Enter symbol (e.g., BTCUSDT): ").upper()
    side = input("Enter side (Buy/Sell): ").capitalize()
    order_type = input("Enter order type (market/limit/stop-limit): ").lower()
    quantity = float(input("Enter quantity: "))

    if order_type == "limit":
        price = float(input("Enter limit price: "))
        return symbol, side, order_type, quantity, price
    elif order_type == "stop-limit":
        stop_price = float(input("Enter stop price: "))
        limit_price = float(input("Enter limit price: "))
        return symbol, side, order_type, quantity, stop_price, limit_price
    else:
        return symbol, side, order_type, quantity

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    bot = BasicBot()
    user_input = get_user_input()

    if len(user_input) == 4:
        symbol, side, order_type, quantity = user_input
        if order_type == "market":
            bot.place_market_order(symbol, side, quantity)
    elif len(user_input) == 5:
        symbol, side, order_type, quantity, price = user_input
        if order_type == "limit":
            bot.place_limit_order(symbol, side, quantity, price)
    elif len(user_input) == 6:
        symbol, side, order_type, quantity, stop_price, limit_price = user_input
        if order_type == "stop-limit":
            bot.place_stop_limit_order(symbol, side, quantity, stop_price, limit_price)
