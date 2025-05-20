from prefix_lookup import load_prefix_data, lookup_operator

load_prefix_data()

test_numbers = [
    "9876543210", "8123456789", "7012345678", "6023456789", "9999999999"
]

for number in test_numbers:
    result = lookup_operator(number)
    print(f"{number} => {result if result else 'Not Found in Prefix DB'}")
