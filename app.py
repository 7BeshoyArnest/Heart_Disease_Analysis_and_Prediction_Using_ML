from flask import Flask, request, jsonify, Response, json
from collections import OrderedDict
import joblib
import numpy as np
from flasgger import Swagger

# Initialize Flask app
app = Flask(__name__)
swagger = Swagger(app)

# Load the trained model
model = joblib.load('model_joblib_heart')


@app.route('/')
def home():
    return " Heart Disease Prediction."


@app.route('/predict', methods=['POST'])
def predict():
    """
    Predict whether a patient has heart disease or not.
    This endpoint takes patient data and returns a prediction.
    ---
    tags:
      - Heart Disease Prediction
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - age
            - sex
            - cp
            - trestbps
            - chol
            - fbs
            - restecg
            - thalach
            - exang
            - oldpeak
            - slope
            - ca
            - thal
          properties:
            age:
              type: number
              example: 63
            sex:
              type: number
              example: 1
            cp:
              type: number
              example: 3
            trestbps:
              type: number
              example: 145
            chol:
              type: number
              example: 233
            fbs:
              type: number
              example: 1
            restecg:
              type: number
              example: 0
            thalach:
              type: number
              example: 150
            exang:
              type: number
              example: 0
            oldpeak:
              type: number
              example: 2.3
            slope:
              type: number
              example: 0
            ca:
              type: number
              example: 0
            thal:
              type: number
              example: 1
    responses:
      200:
        description: Prediction result
        schema:
          type: object
          properties:
            Exited:
              type: integer
              example: 0
    """

    data = request.get_json()

    # List of required fields
    required_fields = [
        'age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg',
        'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal'
    ]

    # Check for missing fields
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400

        # Check for empty or null values
        if data[field] is None or (isinstance(data[field], str) and not data[field].strip()):
            return jsonify({"error": f"Field '{field}' cannot be empty"}), 400

    # Type validation
    numeric_fields = [
        'age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg',
        'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal'    
    ]

    for field in numeric_fields:
        if not isinstance(data[field], (int, float)):
            return jsonify({"error": f"Field '{field}' must be a number"}), 400

    
    
    # Arrange features exactly as the model was trained
    features = np.array([[
        data['age'],
        data['sex'],
        data['cp'],         
        data['trestbps'],
        data['chol'],
        data['fbs'],
        data['restecg'],
        data['thalach'],
        data['exang'],
        data['oldpeak'],
        data['slope'],
        data['ca'],
        data['thal']
    ]])

    # Make prediction safely
    try:
        prediction = model.predict(features)
    except Exception as e:
        return jsonify({"error": f"Model prediction failed: {str(e)}"}), 500

    
    if int(prediction[0]) == 0:
        data = OrderedDict([
            ('predict', int(prediction[0])),
            ('Description', 'the patient does not have Heart Disease')
        ])
    else:
        data = OrderedDict([
            ('predict', int(prediction[0])),
            ('Description', 'the patient has Heart Disease')
        ])

    return Response(json.dumps(data), mimetype='application/json')


if __name__ == "__main__":
    app.run(port=5000, debug=True)

