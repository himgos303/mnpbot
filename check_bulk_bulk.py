from predict_operator import predict_operator

bulk_numbers = [
    "9876543210",
    "8123456789",
    "7012345678",
    "6283456789",
    "9988776655"
]

for num in bulk_numbers:
    operator, circle = predict_operator(num)
    print(f"{num} => Operator: {operator}, Circle: {circle}")
