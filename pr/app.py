import streamlit as st
import numpy as np
import pandas as pd
from logistic_regression_manual import LogisticRegressionManual
import joblib



st.set_page_config(
    
    page_title="Heart Disease Prediction",
    layout="centered"
)

st.title("Heart Disease Prediction System")
st.write("Enter your health details to predict heart disease risk.")




@st.cache_resource
@st.cache_resource
def load_model_and_scaler():

    df = pd.read_csv(
        "C:\\AI-ML\\MLProject\\Data\\preprocessed_data.csv"
    )

    FEATURE_COLUMNS = df.drop("cardio", axis=1).columns.tolist()
    SCALE_COLS = ['height','weight','ap_hi','ap_lo','BMI']

    X = df[FEATURE_COLUMNS].values
    y = df["cardio"].values

    model = LogisticRegressionManual(
        learning_rate=0.01,
        epochs=400
    )
    model.fit(X, y)

    scaler = joblib.load("scaler.pkl")

    return model, FEATURE_COLUMNS, SCALE_COLS, scaler



model, FEATURE_COLUMNS, SCALE_COLS, scaler = load_model_and_scaler()


with st.form("user_input_form"):
    st.subheader("🧍 Personal & Health Details")

    gender = st.selectbox("Gender", ["Female", "Male"])
    age_years = st.number_input("Age (years)", 1, 120, 30)

    height = st.number_input("Height (cm)", 100, 250, 165)
    weight = st.number_input("Weight (kg)", 30, 200, 70)

    ap_hi = st.number_input("Systolic BP", 70, 250, 120)
    ap_lo = st.number_input("Diastolic BP", 40, 200, 80)

    cholesterol = st.selectbox(
        "Cholesterol Level",
        [1, 2, 3],
        format_func=lambda x: {
            1: "Normal",
            2: "Above Normal",
            3: "Well Above Normal"
        }[x]
    )

    gluc = st.selectbox(
        "Glucose Level",
        [1, 2, 3],
        format_func=lambda x: {
            1: "Normal",
            2: "Above Normal",
            3: "Well Above Normal"
        }[x]
    )

    smoke = st.radio("Do you smoke?", [0, 1], format_func=lambda x: "Yes" if x else "No")
    alco = st.radio("Do you consume alcohol?", [0, 1], format_func=lambda x: "Yes" if x else "No")
    active = st.radio("Are you physically active?", [0, 1], format_func=lambda x: "Yes" if x else "No")

    submitted = st.form_submit_button("🔍 Predict")


if submitted:

    # Encode gender
    gender_val = 1 if gender == "Male" else 0

    # Calculate BMI
    bmi = weight / ((height / 100) ** 2)

    # Build input dictionary
    input_dict = {
        "age_years": age_years,
        "gender": gender_val,
        "height": height,
        "weight": weight,
        "ap_hi": ap_hi,
        "ap_lo": ap_lo,
        "cholesterol": cholesterol,
        "gluc": gluc,
        "smoke": smoke,
        "alco": alco,
        "active": active,
        "BMI": bmi
    }

    # Create user input array in correct feature order
    user_df = pd.DataFrame([input_dict])
    user_df[SCALE_COLS] = scaler.transform(user_df[SCALE_COLS])

    user_data = user_df[FEATURE_COLUMNS].values


    st.write("🔍 Scaled user input:", user_data)
    st.write("🔍 z value:", np.dot(user_data, model.weights) + model.bias)


    # Make prediction
    probability = model.predict_proba(user_data)[0]


    st.subheader("📊 Prediction Result")

    st.metric(
        "Heart Disease Risk Probability",
        f"{probability * 100:.2f}%"
    )

    if probability >= 0.5:
        st.error("⚠️ High risk of heart disease detected.")
    else:
        st.success("✅ Low risk of heart disease detected.")

    st.write("🔍 Standardized user input:", user_data)
