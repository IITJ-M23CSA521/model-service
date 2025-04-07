# model_service.py
from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/')
def home():
    return "Model Service is Running!"

@app.route('/predict')
def predict():
    return jsonify({"recommended_pods": random.randint(1, 5)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
