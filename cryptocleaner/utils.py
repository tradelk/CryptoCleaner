def summarize(df):
    """Print simple crypto data summary."""
    print("\n📊 Crypto Data Summary:")
    print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
    if "close" in df.columns:
        print(f"Close price range: {df['close'].min()} → {df['close'].max()}")
    if "volume" in df.columns:
        print(f"Volume range: {df['volume'].min()} → {df['volume'].max()}")

