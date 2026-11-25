from itertools import combinations
from pathlib import Path
from src.data_loader import read_transactions
from src.visualization import plot_frequent_itemsets

BASE_DIR = Path(__file__).resolve().parent

DATA_FILE = BASE_DIR / "data" / "Transactions.xlsx"

transactions = read_transactions(DATA_FILE)

def temp_apriori(transactions, min_support):
    """حساب مؤقت للـ L1 و L2 بس. هتتشال لما apriori.py يخلص."""
    items = sorted({i for t in transactions for i in t})
    candidates = [frozenset([i]) for i in items]
    candidates += [frozenset(c) for c in combinations(items, 2)]

    frequent = {}
    for c in candidates:
        support = sum(c <= t for t in transactions) / len(transactions)
        if support >= min_support:
            frequent[c] = support
    return frequent


def main():
    transactions = read_transactions(DATA_FILE)
    
    # temporary
    MIN_SUPPORT = 0.2
    frequent_itemsets = temp_apriori(transactions, MIN_SUPPORT)

    plot_frequent_itemsets(frequent_itemsets)


if __name__ == "__main__":
    main()