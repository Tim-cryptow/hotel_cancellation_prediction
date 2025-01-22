import os
import joblib
import pandas as pd
import json
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Loading the model and associated files
try:
    model = joblib.load('models/hotel_cancellation_model.joblib')
    scaler = joblib.load('models/scaler.joblib')
    with open('models/feature_columns.json', 'r') as f:
        feature_columns = json.load(f)
except Exception as e:
    print(f"Error loading model files: {str(e)}")
    model = None
    scaler = None
    feature_columns = []

@app.route('/predict', methods=['POST'])
def predict_cancellation():
    if model is None or scaler is None:
        return jsonify({'error': 'Model not loaded correctly'}), 500

    booking_data = request.json
    
    # Creating DataFrame with the required columns
    df = pd.DataFrame([booking_data])
    
    # Creating dummy variables
    df = pd.get_dummies(df, drop_first=True)
    
    for col in feature_columns:
        if col not in df.columns:
            df[col] = 0
            
    # Reordering columns to match training data
    df = df[feature_columns]
    
    # Scaling the features
    scaled_features = scaler.transform(df)
    
    # Getting prediction probability
    cancellation_prob = model.predict_proba(scaled_features)[0][1]
    
    return jsonify({'cancellation_probability': float(cancellation_prob)})

@app.route('/', methods=['GET'])
def home():
    return "Hotel Cancellation Predictor is running. Use /predict endpoint for predictions."

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
