import pandas as pd

def load_data():
    data = {
        "date": ["2025-01-01", "2025-01-02", "2025-01-03"],
        "store": ["A", "B", "A"],
        "sales": [1200, 1500, 1100]
    }
    return pd.DataFrame(data)

def analyze_sales(df):
    total = df["sales"].sum()
    by_store = df.groupby("store")["sales"].sum()
    return total, by_store

if __name__ == "__main__":
    df = load_data()
    total, by_store = analyze_sales(df)

    print("Total Sales:", total)
    print("\nSales by Store:")
    print(by_store)