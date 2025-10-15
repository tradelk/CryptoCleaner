import pandas as pd

def add_indicators(df, window=5):
    """Add simple analytics like % change and rolling average."""
    if "close" in df.columns:
        df["returns_%"] = df["close"].pct_change() * 100
        df["rolling_avg"] = df["close"].rolling(window=window).mean()
    return df

