import os
import pandas as pd
import yfinance as yf
from fredapi import Fred
from pathlib import Path

data_path = Path("src/data")
data_path.mkdir(parents=True, exist_ok=True)

fred = Fred(os.getenv("FRED_API_KEY"))

START_DATE = "2015-01-01"
END_DATE = "2025-12-31"

yf_ticker = {
    "btc": "BTC-USD",
    "eth": "ETH-USD",
    "dow": "^DJI",
    "sp500": "^GSPC",
    "nasdaq": "^IXIC"
}

for key, ticker in yf_ticker.items():
    df = yf.download(
        ticker,
        start=START_DATE,
        end=END_DATE,
        auto_adjust=False,
        progress=False
    )

    df = df[["Close"]]
    df.columns = [key]
    df.index.name = "Date"
    df.to_csv(data_path / f"{key}_data.csv")
    print(f"Saved {key} data.")


fred_vars = {
    "cpi": "CPIAUCSL",
    "fedfunds": "FEDFUNDS",
    "m2": "M2SL",
    "usdindex": "DTWEXBGS"
}

start_date = pd.to_datetime(START_DATE)
end_date = pd.to_datetime(END_DATE)

for key, series_id in fred_vars.items():
    data = fred.get_series(series_id)
    df = pd.DataFrame(data, columns=[key])
    df.index = pd.to_datetime(df.index)
    df = df[(df.index >= start_date) & (df.index <= end_date)]
    df.index.name = "Date"
    df.to_csv(data_path / f"{key}_data.csv")
    print(f"Saved {key} data.")
