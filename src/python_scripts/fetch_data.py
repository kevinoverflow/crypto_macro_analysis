import os
import pandas as pd
import yfinance as yf
from fredapi import Fred
from pathlib import Path

data_path = Path("src/data")
data_path.mkdir(parents=True, exist_ok=True)

fred = Fred(os.getenv("FRED_API_KEY"))

yf_ticker= {
    "btc": "BTC-USD",
    "eth": "ETH-USD",
    "dow": "^DJI",
    "sp500": "^GSPC",
    "nasdaq": "^IXIC"
}

for key, ticker in yf_ticker.items():
    df = yf.download(ticker, start="2015-01-01", end="2025-01-01")
    df.to_csv(data_path / f"{key}_data.csv")
    print(f"Saved {key} data.")

fred_vars = {
    "cpi": "CPIAUCSL",
    "fedfunds": "FEDFUNDS",
    "m2": "M2SL",
    "usdindex": "DTWEXBGS"
}

for key, series_id in fred_vars.items():
    data = fred.get_series(series_id)
    df = pd.DataFrame(data, columns=[key])
    df.index = pd.to_datetime(df.index)
    df.to_csv(data_path / f"{key}_data.csv")
    print(f"Saved {key} data.")

