❤️ Heart Disease Analysis and Prediction
This project analyzes and predicts the likelihood of heart disease in patients using machine learning 
algorithms. It includes exploratory data analysis (EDA), feature engineering, model training, and evaluation based on medical attributes.

🧠 Objective
To build a reliable prediction model that identifies patients at risk of heart disease based on various clinical 
features such as age, cholesterol levels, blood pressure, and more. This project aids in early detection and preventive healthcare.

📁 Dataset
Source: https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction

Records: ~300 entries

Target: target (1 = disease, 0 = no disease)

Features Include:
Age

Sex

Chest Pain Type

Resting Blood Pressure

Serum Cholesterol

Fasting Blood Sugar

Resting ECG

Max Heart Rate

Exercise Induced Angina

ST Depression

Number of Major Vessels

Thalassemia

Target (0/1)

📊 Exploratory Data Analysis (EDA)
Checked for missing values and data types

Visualized class distribution, age distribution, and feature correlations

Used heatmaps and pair plots to understand relationships

Assessed feature importance

⚙️ Preprocessing
Encoding categorical features

Feature scaling using StandardScaler

Handling imbalance if present

Splitting data into training and test sets

🤖 Machine Learning Models
The following models were trained and evaluated:

Logistic Regression

K-Nearest Neighbors (KNN)

Decision Tree Classifier

Random Forest Classifier

Support Vector Machine (SVM)

XGBoost

📈 Evaluation Metrics
To ensure effective performance, the models were evaluated using:

Accuracy

Precision

Recall

F1 Score

Confusion Matrix

ROC-AUC Curve

🏆 Best Model Performance

| Model         | Accuracy | F1 Score | ROC-AUC |
| ------------- | -------- | -------- | ------- |
| XGBoost       | ✅ High   | ✅ High   | ✅ High  |
| Random Forest | High     | High     | High    |
| SVM           | Good     | Moderate | Good    |


XGBoost and Random Forest outperformed other models in precision and recall, making them most suitable for medical predictions.
