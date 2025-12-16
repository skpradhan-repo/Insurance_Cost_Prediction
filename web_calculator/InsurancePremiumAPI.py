from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load model
model = joblib.load("xgboost_model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json  # input data as JSON
    X_input = pd.DataFrame([data])  # convert to DataFrame
    # Apply scaler if needed
    # X_input[scaled_features] = scaler.transform(X_input[scaled_features])
    prediction = model.predict(X_input)[0]
    return jsonify({"predicted_premium": float(prediction)})

if __name__ == "__main__":
    app.run(debug=True)