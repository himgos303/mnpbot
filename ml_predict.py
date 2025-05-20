# ml_predict.py

from predict_operator import predict_operator


def predict_operator_fallback(mobile_number):
    prefix = mobile_number[:4]
    try:
        prediction = predict_operator(prefix)
        return prediction
    except Exception as e:
        print(f"ML Prediction Error: {e}")
        return predict_operator(mobile_number)
