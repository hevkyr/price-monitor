

import time
import requests
import json
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()


def load_config():
    with open("config.json", "r", encoding="utf-8") as f:
        return json.load(f)


ALPHA_VANTAGE_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")


def get_stock_price(symbol: str):
    url = "https://www.alphavantage.co/query"
    params = {
        "function": "GLOBAL_QUOTE",
        "symbol": symbol,
        "apikey": ALPHA_VANTAGE_API_KEY,
    }
    response = requests.get(url, params=params, timeout=15)
    data = response.json()
    quote = data.get("Global Quote", {})
    return float(quote["05. price"])


def get_crypto_price(symbol: str):
    url = "https://api.binance.com/api/v3/ticker/price"
    response = requests.get(url, params={"symbol": symbol}, timeout=15)
    data = response.json()
    return float(data["price"])


def send_telegram_message(message: str):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=payload, timeout=15)


def monitor():
    config = load_config()
    interval = config.get("interval", 300)
    last_alerts = {}

    while True:
        for asset in config["assets"]:
            symbol = asset["symbol"]
            asset_type = asset.get("type", "stock")
            above = asset.get("alert_above")
            below = asset.get("alert_below")

            try:
                if asset_type == "crypto":
                    price = get_crypto_price(symbol)
                else:
                    price = get_stock_price(symbol)

                now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

                if above and price >= above:
                    key = f"{symbol}_above"
                    if not last_alerts.get(key):
                        send_telegram_message(f"🚀 {symbol} above target: {price}")
                        last_alerts[key] = True
                else:
                    last_alerts[f"{symbol}_above"] = False

                if below and price <= below:
                    key = f"{symbol}_below"
                    if not last_alerts.get(key):
                        send_telegram_message(f"📉 {symbol} below target: {price}")
                        last_alerts[key] = True
                else:
                    last_alerts[f"{symbol}_below"] = False

                print(f"[{now}] {symbol}: {price}")

            except Exception as e:
                print(f"Error processing {symbol}: {e}")

        time.sleep(interval)


if __name__ == "__main__":
    monitor()


# dashboard.py
import streamlit as st

st.set_page_config(page_title="Price Monitor Dashboard")
st.title("📈 Price Monitor Dashboard")
st.write("Monitoramento de ações e criptomoedas em tempo real.")


# .env example
# ALPHA_VANTAGE_API_KEY=your_key
# TELEGRAM_TOKEN=your_bot_token
# CHAT_ID=your_chat_id


# config.json example
# {
#   "interval": 300,
#   "assets": [
#     {
#       "symbol": "AAPL",
#       "type": "stock",
#       "alert_above": 250,
#       "alert_below": 180
#     },
#     {
#       "symbol": "BTCUSDT",
#       "type": "crypto",
#       "alert_above": 100000,
#       "alert_below": 85000
#     }
#   ]
# }


# requirements.txt
# requests
# python-dotenv
# streamlit


# Dockerfile
# FROM python:3.11-slim
# WORKDIR /app
# COPY . .
# RUN pip install -r requirements.txt
# CMD ["python", "main.py"]
