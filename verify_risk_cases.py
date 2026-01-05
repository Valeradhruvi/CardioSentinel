import pandas as pd
import joblib
from sklearn.linear_model import LogisticRegression
import numpy as np

def verify_risk():
    # Load data and train model (replicating app.py logic)
    print("Loading data and training model...")
    df = pd.read_csv("Data/preprocessed_data.csv")
    FEATURE_COLUMNS = df.drop("cardio", axis=1).columns.tolist()
    SCALE_COLS = ['height', 'weight', 'ap_hi', 'ap_lo', 'BMI']
    
    X = df[FEATURE_COLUMNS].values
    y = df["cardio"].values
    
    model = LogisticRegression(max_iter=1000)
    model.fit(X, y)
    
    scaler = joblib.load("scaler.pkl")
    
    # Define Test Cases
    print("\nRunning Test Cases...")
    
    # Case 1: Likely Low Risk (Young, normal BMI, normal BP)
    # values: age=25, gender=0(F), height=170, weight=60, ap_hi=110, ap_lo=70, chol=1, gluc=1, smoke=0, alco=0, active=1
    # BMI = 60 / (1.7^2) = 20.76
    low_risk_input = {
        "age_years": 25, "gender": 0, "height": 170, "weight": 60, 
        "ap_hi": 110, "ap_lo": 70, "cholesterol": 1, "gluc": 1, 
        "smoke": 0, "alco": 0, "active": 1, "BMI": 20.76
    }
    
    # Case 2: Likely High Risk (Older, obese, high BP, smoker)
    # values: age=65, gender=1(M), height=175, weight=100, ap_hi=160, ap_lo=100, chol=3, gluc=3, smoke=1, alco=1, active=0
    # BMI = 100 / (1.75^2) = 32.65
    high_risk_input = {
        "age_years": 65, "gender": 1, "height": 175, "weight": 100, 
        "ap_hi": 160, "ap_lo": 100, "cholesterol": 3, "gluc": 3, 
        "smoke": 1, "alco": 1, "active": 0, "BMI": 32.65
    }
    
    cases = [("Low Risk Scenario", low_risk_input), ("High Risk Scenario", high_risk_input)]
    
    for name, input_data in cases:
        user_df = pd.DataFrame([input_data])
        user_df[SCALE_COLS] = scaler.transform(user_df[SCALE_COLS])
        user_data = user_df[FEATURE_COLUMNS].values
        
        # Original Buggy Way (to demo)
        # prob_buggy = model.predict_proba(user_data)[0] * 100 
        
        # Users fixed way
        prob_positive = model.predict_proba(user_data)[0][1] * 100
        
        label = "HIGH RISK" if prob_positive >= 50 else "LOW RISK"
        
        print(f"\n{name}:")
        print(f"  Probability: {prob_positive:.2f}%")
        print(f"  Label: {label}")

if __name__ == "__main__":
    verify_risk()
