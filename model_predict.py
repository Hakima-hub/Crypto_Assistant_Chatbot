import joblib
import numpy as np

model = joblib.load("models/final_model.pkl")
scaler = joblib.load("models/label_encoder.pkl")

def predict_trend(features):
    """Predict trend using trained ML model."""
    features_scaled = scaler.transform(np.array(features).reshape(1, -1))
    return model.predict(features_scaled)[0]
