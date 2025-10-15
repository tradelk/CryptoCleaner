from cryptocleaner.cleaner import clean_crypto_data
import argparse

def main():
    parser = argparse.ArgumentParser(description="🪙 CryptoCleaner — clean & analyze crypto CSVs")
    parser.add_argument("input_file", help="Path to input CSV file (e.g., BTCUSDT.csv)")
    parser.add_argument("-o", "--output", default="cleaned_crypto.csv", help="Output file name")
    parser.add_argument("--fillna", type=float, default=0.0, help="Value to fill missing numeric data")
    parser.add_argument("--window", type=int, default=5, help="Rolling average window size (days)")
    args = parser.parse_args()

    clean_crypto_data(args.input_file, args.output, args.fillna, args.window)
    print(f"✅ Cleaned data saved to: {args.output}")

if __name__ == "__main__":
    main()

