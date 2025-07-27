# Binance_bot
A Python-based automated trading bot built for the Binance Futures Testnet (USDT-M). This bot allows users to place Market, Limit, and Stop-Limit orders using the Binance API, with built-in logging, error handling, and a clean CLI interface.

🚀 Features
✅ Supports Buy & Sell Orders

✅ Market & Limit Orders

✅ Stop-Limit Order (Bonus)

✅ Binance Futures Testnet Integration

✅ Clean Command-Line Interface (CLI)

✅ API Logging & Error Handling

✅ Environment Variable Support via .env

✅ Reusable Bot Class (BasicBot)

🧠 Tech Stack
Python 3.x

python-binance

dotenv, logging

⚙️ How It Works
Loads API keys from .env

Initializes Binance Futures Testnet client

Accepts user input (order type, side, symbol, qty)

Executes the appropriate order type

Logs request/response and shows success/failure
