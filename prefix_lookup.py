# prefix_lookup.py

import csv
import os

# Supported CSV files
CSV_FILES = [
    "6xxx-in-mob-prefix.csv",
    "7xxx-in-mob-prefix.csv",
    "8xxx-in-mob-prefix.csv",
    "9xxx-in-mob-prefix.csv"
]

# The main dictionary to store prefix mappings
prefix_data = {}

def load_prefix_data():
    """Loads prefix data from all CSV files into a dictionary."""
    for file in CSV_FILES:
        if not os.path.exists(file):
            print(f"⚠️ File not found: {file}")
            continue

        with open(file, mode='r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                prefix = row.get("series")
                if prefix and prefix not in prefix_data:
                    prefix_data[prefix] = {
                        "operator": row.get("operator"),
                        "circle": row.get("circle")
                    }

def lookup_operator(mobile_number: str):
    """Takes a full 10-digit number and returns operator/circle info from prefix DB."""
    if len(mobile_number) != 10 or not mobile_number.isdigit():
        return None

    prefix = mobile_number[:4]
    return prefix_data.get(prefix, None)
