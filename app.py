from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)
model = joblib.load('fraud_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    values = [float(request.form[f'v{i}']) for i in range(1, 5)]  # Simplified to 4 features
    features = [np.array(values)]
    prediction = model.predict(features)
    result = 'Fraudulent Transaction' if prediction[0] == 1 else 'Legitimate Transaction'
    return render_template('result.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True)
