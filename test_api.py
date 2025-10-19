import requests
import json

# API endpoint
url = "http://127.0.0.1:5000/predict"

# Example payload (features in correct order)
data = {
    "age": 63,
    "sex": 1,
    "cp": 3,        
    "trestbps": 145,
    "chol": 233,
    "fbs": 1,
    "restecg": 0,
    "thalach": 150,
    "exang": 0,
    "oldpeak": 2.3,
    "slope": 0,
    "ca": 0,
    "thal": 1
}

# Send POST request
response = requests.post(url, json=data)

# Print response
print("Status Code:", response.status_code)
print("Response JSON:", json.dumps(response.json(), indent=2))
