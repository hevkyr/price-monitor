# 📈 Price Monitor

<div align="center">

**Real-time stock & crypto price monitoring with Telegram alerts**

🐍 Python • 📊 Streamlit • 🤖 Telegram • 🐳 Docker

</div>

---

## 📖 About

`price-monitor` is a Python application for monitoring **stocks and cryptocurrencies** in real time.

The project:

- Fetches stock prices using **Alpha Vantage**
- Fetches crypto prices using **Binance API**
- Sends price alerts through **Telegram**
- Supports configurable thresholds
- Includes a simple dashboard built with **Streamlit**

Perfect for tracking assets automatically without checking charts all day.

---

## ✨ Features

- 📈 Stock monitoring via Alpha Vantage
- ₿ Crypto monitoring via Binance
- 🚨 Telegram alerts
- 🔒 Secrets stored in `.env`
- 📊 Web dashboard with Streamlit
- 🐳 Docker support
- ⏱ Configurable polling interval

---


## 📁 Project Structure

```text
price-monitor/
├── monitor.py
└── README.md
```

---

## 🚀 Installation

Clone repository:

```bash
git clone https://github.com/hevkyr/price-monitor.git
cd price-monitor
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ⚙ Configuration

Create a `.env` file:

```env
ALPHA_VANTAGE_API_KEY=your_api_key
TELEGRAM_TOKEN=your_bot_token
CHAT_ID=your_chat_id
```

Example `config.json`:

```json
{
  "interval": 300,
  "assets": [
    {
      "symbol": "AAPL",
      "type": "stock",
      "alert_above": 250,
      "alert_below": 180
    },
    {
      "symbol": "BTCUSDT",
      "type": "crypto",
      "alert_above": 100000,
      "alert_below": 85000
    }
  ]
}
```

---

## ▶ Usage

Run monitor:

```bash
python main.py
```

Example output:

```text
[2026-05-03 02:10:00 UTC] AAPL: 212.55
[2026-05-03 02:10:00 UTC] BTCUSDT: 96420.12
```

---

## 🤖 Telegram Alerts

Example alert:

```text
🚀 BTCUSDT above target
Price: 100250.45
```

or

```text
📉 AAPL below target
Price: 178.21
```

---

## 📊 Dashboard

Launch dashboard:

```bash
streamlit run dashboard.py
```

Open browser:

```text
http://localhost:8501
```

---

## 🐳 Docker

Build image:

```bash
docker build -t price-monitor .
```

Run container:

```bash
docker run --env-file .env price-monitor
```

---

## 🔌 APIs Used

- Alpha Vantage (stocks)
- Binance Public API (crypto)
- Telegram Bot API

---

## ⚠ Notes

- Alpha Vantage free tier has rate limits
- Binance symbols must use exchange format (example: `BTCUSDT`)
- Keep `.env` private

---

## 📜 License

MIT License
