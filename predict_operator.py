# predict_operator.py

import pandas as pd

def safe_value(val):
    """Return 'Unknown' for NaN or None."""
    if pd.isna(val) or val is None:
        return "Unknown"
    return str(val).strip()

def load_prefix_data():
    df = pd.read_csv("prefix_database.csv")

    # Create prefix column if not already present
    if 'prefix' not in df.columns:
        df['prefix'] = df['series'].astype(str).str[:4]

    df['prefix'] = df['prefix'].astype(str).str.strip()
    return df

prefix_data = load_prefix_data()

def predict_operator(mobile_number):
    mobile_number = str(mobile_number).strip()

    for length in range(4, 0, -1):
        prefix = mobile_number[:length]
        matched_rows = prefix_data[prefix_data['prefix'] == prefix]
        if not matched_rows.empty:
            operator = safe_value(matched_rows.iloc[0]['operator'])
            circle = safe_value(matched_rows.iloc[0]['circle'])
            return operator, circle

    return "Unknown", "Unknown"

def check_bulk_numbers(file_path):
    with open(file_path, 'r') as f:
        numbers = [line.strip() for line in f if line.strip()]
    
    for num in numbers:
        operator, circle = predict_operator(num)
        print(f"{num} => Operator: {operator}, Circle: {circle}")

if __name__ == "__main__":
    check_bulk_numbers("numbers.txt")
