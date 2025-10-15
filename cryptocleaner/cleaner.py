import pandas as pd
from .analyzer import add_indicators
from .utils import summarize

def clean_crypto_data(input_file, output_file="cleaned_crypto.csv", fillna=0.0, window=5):
    """Clean crypto CSV: fix timestamps, remove duplicates, fill NA, add analytics."""
    try:
        df = pd.read_csv(input_file)

        # Basic cleaning
        df = df.drop_duplicates()
        if "timestamp" in df.columns:
            df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
            df = df.sort_values("timestamp")

        # Fill missing numeric data
        df = df.fillna(fillna)

        # Add derived indicators
        df = add_indicators(df, window=window)

        # Save result
        df.to_csv(output_file, index=False)

        summarize(df)

    except Exception as e:
        print(f"❌ Error processing file: {e}")

