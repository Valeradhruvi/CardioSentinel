# CardioSentinel

**End-to-End Cardiovascular Risk Prediction Web Application**

CardioSentinel is a smart, user-friendly tool designed to assess heart health risks using machine learning. It analyzes user data—like age, weight, blood pressure, and lifestyle habits—to provide a real-time risk assessment and personalized health advice.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-ff4b4b)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Model-orange)

## 🚀 Features

- **Smart Prediction Engine**: Built on a Logistic Regression model trained on 70,000+ patient records (73% accuracy).
- **Interactive Dashboard**:
    - Real-time biometric scanning.
    - Visual analytics of risk factors.
    - "Dark/Light" Theme Toggle for accessibility.
- **User-Friendly Interface**:
    - Simplified English language for easy understanding.
    - Clear "High Risk" / "Low Risk" feedback with visual alerts.
    - Celebration animations for good health results!
- **Personalized Advice**: Dynamic health tips based on your specific inputs (e.g., customized advice for smokers or high BMI).
- **Comprehensive Resources**:
    - **Analytics**: Understand how risk is calculated.
    - **Guidelines**: Simple diet and exercise tips for a healthy heart.
    - **Neural Profile**: Technical details about the underlying model.

## 🛠️ Tech Stack

- **Frontend**: Streamlit (Python) with custom CSS/HTML styling.
- **Backend/ML**: Python, Scikit-Learn, Pandas, Numpy, Joblib.
- **Data**: Cardiovascular Disease dataset (70,000 records).

## 📦 Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/Valeradhruvi/CardioSentinel.git
    cd CardioSentinel
    ```

2.  **Create a virtual environment** (recommended):
    ```bash
    python -m venv venv
    # Windows
    .\venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: Ensure you have a `requirements.txt` file or install manually: `pip install streamlit pandas numpy scikit-learn joblib`)*

## 🏃 Usage

Run the application locally using Streamlit:

```bash
streamlit run app.py
```

The app will open in your default web browser at `http://localhost:8501`.

## 📂 Project Structure

- `app.py`: Main application file containing the Dashboard and Prediction logic.
- `about.py`: Technical overview and model details.
- `analysis.py`: Analytics page explaining risk factors.
- `guidelines.py`: Health tips and protocols.
- `verify_risk_cases.py`: Script for testing model predictions.
- `Data/`: Directory containing datasets.

## ⚠️ Disclaimer

**This tool is for informational purposes only.**
CardioSentinel provides statistical estimations based on population data. It **does not** constitute a medical diagnosis. Always consult a licensed cardiologist or healthcare professional for accurate medical advice.

---
*Built with ❤️ for Heart Health Awareness*
