from ml_predict import predict_operator_fallback

numbers = [
    "9876543210",
    "8123456789",
    "7012345678",
    "6283456789",
    "9988776655"
]

for num in numbers:
    operator, circle = predict_operator_fallback(num)
    print(f"{num} => Operator: {operator}, Circle: {circle}")
