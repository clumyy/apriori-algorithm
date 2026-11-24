from pathlib import Path
from src.data_loader import read_transactions

BASE_DIR = Path(__file__).resolve().parent

DATA_FILE = BASE_DIR / "data" / "Transactions.xlsx"

transactions = read_transactions(DATA_FILE)
print(transactions)