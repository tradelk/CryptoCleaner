# 🪙 CryptoCleaner — Clean & Analyze Crypto Market CSVs

A simple Python tool by [@tradelk](https://github.com/tradelk) to quickly clean, process, and summarize crypto market CSV files.  
Removes duplicates, fixes timestamps, fills missing values, and even adds basic indicators like % returns and rolling averages.

---

## 🚀 Usage

```bash
# Install dependencies
pip install -r requirements.txt

# Run the cleaner
python main.py examples/sample_crypto.csv -o cleaned_crypto.csv --window 5

