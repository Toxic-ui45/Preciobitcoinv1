import yfinance as yf
from binance.client import Client
import datetime

# Initialize Binance client (no API key needed for public data)
binance_client = Client()

def get_realtime_btc_price():
    """Fetch real-time Bitcoin price from Binance."""
    ticker = binance_client.get_symbol_ticker(symbol="BTCUSDT")
    price = float(ticker['price'])
    return price

def get_historical_btc_variation(period="3mo"):
    """
    Fetch historical Bitcoin price data from Yahoo Finance and calculate variation.
    period: string like '1mo', '3mo', '1y', etc.
    Returns percentage change over the period.
    """
    btc = yf.Ticker("BTC-USD")
    hist = btc.history(period=period)
    if hist.empty:
        return None
    start_price = hist['Close'].iloc[0]
    end_price = hist['Close'].iloc[-1]
    variation = ((end_price - start_price) / start_price) * 100
    return variation

def main():
    realtime_price = get_realtime_btc_price()
    print(f"Real-time BTC price from Binance: ${realtime_price:,.2f}")

    variation_3mo = get_historical_btc_variation("3mo")
    if variation_3mo is not None:
        print(f"BTC price variation over last 3 months: {variation_3mo:.2f}%")
    else:
        print("Could not fetch historical data.")

if __name__ == "__main__":
    main()
