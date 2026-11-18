import yfinance as yf
import pandas as pd
from pathlib import Path

TICKERS = [
    "SPY", "QQQ", "IWM", "EFA", "EEM", "TLT", "IEF", "GLD", "DBC", "VNQ"
]

DATA_DIR = Path("data/raw")

def download_prices(
    tickers=TICKERS,
    start="2010-01-01"
):
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    prices = yf.download(
        tickers=tickers,
        start=start,
        auto_adjust=True,
        group_by="column",
        progress=False
    )["Close"]

    prices = prices.sort_index()

    prices.to_csv(DATA_DIR / "adjusted_prices.csv")

    return prices

if __name__ == "__main__":
    prices = download_prices()
    print(prices.head())
    print(prices.tail())
    print(prices.shape)
    print(prices.isna().sum())