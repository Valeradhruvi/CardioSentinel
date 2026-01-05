import streamlit as st
import numpy as np
import pandas as pd
import joblib
from logistic_regression_manual import LogisticRegressionManual
from sklearn.linear_model import LogisticRegression

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="CardioSentinel | Smart Diagnostics",
    page_icon="❤️",
    layout="wide"
)

# ---------------- SESSION STATE INIT ---------------- #
if 'current_page' not in st.session_state:
    st.session_state.current_page = "DASHBOARD"
if 'theme' not in st.session_state:
    st.session_state.theme = "dark"

def nav_to(page_name):
    st.session_state.current_page = page_name

def toggle_theme():
    st.session_state.theme = "light" if st.session_state.theme == "dark" else "dark"

# ---------------- THEME ENGINE CSS ---------------- #
theme_css = {
    "dark": {
        "bg": "radial-gradient(at 0% 0%, rgba(124, 58, 237, 0.25) 0, transparent 50%), radial-gradient(at 100% 100%, rgba(6, 182, 212, 0.2) 0, transparent 50%), #020617",
        "text": "#ffffff",
        "card_bg": "rgba(15, 23, 42, 0.6)",
        "card_border": "rgba(255, 255, 255, 0.1)",
        "nav_bg": "rgba(2, 6, 23, 0.95)",
        "sub_text": "#94a3b8",
        "accent": "#7c3aed",
        "accent_vibrant": "#06b6d4",
        "metric_bg": "rgba(255, 255, 255, 0.03)",
        "title_gradient": "linear-gradient(to right, #ffffff 40%, var(--accent-vibrant) 100%)"
    },
    "light": {
        "bg": "radial-gradient(at 0% 0%, rgba(124, 58, 237, 0.15) 0, transparent 50%), radial-gradient(at 100% 100%, rgba(6, 182, 212, 0.12) 0, transparent 50%), #ffffff",
        "text": "#020617",
        "card_bg": "rgba(255, 255, 255, 0.98)",
        "card_border": "rgba(124, 58, 237, 0.25)",
        "nav_bg": "rgba(255, 255, 255, 0.98)",
        "sub_text": "#334155",
        "accent": "#7c3aed",
        "accent_vibrant": "#0891b2",
        "metric_bg": "rgba(124, 58, 237, 0.08)",
        "input_bg": "#f1f5f9",
        "title_gradient": "linear-gradient(to right, #020617 40%, var(--accent) 100%)"
    }
}

t = theme_css[st.session_state.theme]

st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Outfit:wght@300;400;500;600;700;800&display=swap');

    :root {{
        --bg-primary: {t['bg']};
        --text-primary: {t['text']};
        --card-bg: {t['card_bg']};
        --card-border: {t['card_border']};
        --nav-bg: {t['nav_bg']};
        --sub-text: {t['sub_text']};
        --accent: {t['accent']};
        --accent-vibrant: {t['accent_vibrant']};
        --metric-bg: {t['metric_bg']};
        --input-bg: {t.get('input_bg', 'rgba(255,255,255,0.05)')};
        --title-gradient: {t['title_gradient']};
    }}

    html, body, [class*="css"] {{
        font-family: 'Plus Jakarta Sans', sans-serif;
    }}

    .stApp {{
        background: var(--bg-primary);
        background-attachment: fixed;
        color: var(--text-primary);
    }}

    [data-testid="stHeader"] {{ display: none !important; }}
    section[data-testid="stSidebar"] {{ display: none !important; }}
    
    /* Strict Layout Fix */
    .main .block-container {{ 
        padding-top: 0 !important; 
        padding-bottom: 5rem !important;
        max-width: 1400px; 
        margin: 0 auto; 
    }}

    /* --- HI-FI NAVBAR LOGIC --- */
    /* Targeting the first columns block precisely for the navbar */
    [data-testid="stVerticalBlock"] > div:has(div.stButton) {{
        position: relative;
        z-index: 1000;
        background: transparent !important;
        backdrop-filter: none !important;
        -webkit-backdrop-filter: none !important;
        border-bottom: none !important;
        padding: 1.5rem 0;
        margin-top: 0 !important;
        margin-bottom: 2rem;
        box-shadow: none !important;
        display: flex;
        justify-content: center;
    }}

    [data-testid="stHorizontalBlock"] {{
        gap: 0.5rem !important;
        align-items: center;
        max-width: 1350px;
        margin: 0 auto;
        padding-bottom: 0.8rem !important;
        border-bottom: 1px solid var(--card-border) !important;
    }}

    div.stButton > button {{
        background: var(--card-bg) !important;
        color: var(--sub-text) !important;
        border: 1px solid var(--card-border) !important;
        padding: 0 1.8rem !important;
        height: 44px !important;
        border-radius: 50px !important;
        font-weight: 800 !important;
        transition: all 0.4s cubic-bezier(0.23, 1, 0.32, 1) !important;
        font-size: 0.72rem !important;
        text-transform: uppercase !important;
        letter-spacing: 0.1em !important;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.12) !important;
        position: relative;
        overflow: hidden;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }}

    /* Target the LAST button in the horizontal block (Theme Change) */
    [data-testid="stHorizontalBlock"] > div:nth-child(6) button {{
        background: transparent !important;
        border: 1px solid var(--accent-vibrant) !important;
        color: var(--accent-vibrant) !important;
        box-shadow: none !important;
    }}
    
    [data-testid="stHorizontalBlock"] > div:nth-child(6) button:hover {{
        background: var(--accent-vibrant) !important;
        color: {('#000000' if st.session_state.theme == 'dark' else '#ffffff')} !important;
        box-shadow: 0 0 20px var(--accent-vibrant) !important;
        transform: translateY(-2px) !important;
    }}

    div.stButton > button::after {{
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        background: linear-gradient(to bottom, rgba(255,255,255,0.1), transparent);
        opacity: 0;
        transition: opacity 0.3s;
    }}


    div.stButton > button:hover {{
        color: var(--accent-vibrant) !important;
        border-color: var(--accent-vibrant) !important;
        transform: translateY(-3px) scale(1.02);
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1) !important;
    }}

    div.stButton > button:hover::after {{
        opacity: 1;
    }}

    div.stButton > button:active {{
        transform: translateY(1px);
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1) !important;
    }}

    div.stButton > button[kind="primary"] {{
        background: linear-gradient(135deg, var(--accent) 0%, var(--accent-vibrant) 100%) !important;
        color: white !important;
        border: none !important;
        box-shadow: 0 10px 30px -5px rgba(6, 182, 212, 0.5) !important;
        text-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }}

    div.stButton > button[kind="primary"]::before {{
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0; height: 50%;
        background: rgba(255, 255, 255, 0.1);
        pointer-events: none;
    }}

    div.stButton > button[kind="primary"]:hover {{
        box-shadow: 0 15px 40px -5px rgba(6, 182, 212, 0.7) !important;
        filter: brightness(1.1);
    }}

    /* --- CARD SYSTEM --- */
    .card {{
        background: var(--card-bg);
        backdrop-filter: blur(40px);
        -webkit-backdrop-filter: blur(40px);
        border: 1px solid var(--card-border);
        border-radius: 40px;
        padding: 3.5rem;
        box-shadow: 0 40px 100px -20px rgba(0, 0, 0, 0.4);
        margin-bottom: 4rem;
        transition: all 0.4s ease;
        position: relative;
        overflow: hidden;
    }}

    .card::before {{
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 6px;
        background: linear-gradient(90deg, var(--accent), var(--accent-vibrant));
        opacity: 0.8;
    }}

    .card:hover {{
        border-color: var(--accent-vibrant);
        transform: translateY(-3px);
        box-shadow: 0 50px 120px -30px rgba(0, 0, 0, 0.5);
    }}

    .app-title {{
        text-align: center;
        font-size: 5rem;
        font-weight: 900;
        letter-spacing: -0.05em;
        font-family: 'Outfit', sans-serif;
        background: var(--title-gradient);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        line-height: 0.95;
        margin-top: 1.5rem;
        margin-bottom: 0.5rem;
    }}

    .app-subtitle-premium {{
        text-align: center;
        color: var(--accent-vibrant);
        font-size: 0.75rem;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 0.4em;
        margin-top: 0.5rem;
        margin-bottom: 3rem;
        opacity: 0.9;
        text-shadow: 0 0 20px rgba(6, 182, 212, 0.4);
    }}

    /* --- COMPONENTS --- */
    .metric-card {{
        background: var(--metric-bg);
        border: 1px solid var(--card-border);
        padding: 3rem 1.5rem;
        border-radius: 35px;
        text-align: center;
        transition: all 0.5s cubic-bezier(0.19, 1, 0.22, 1);
    }}
    .metric-card:hover {{
        background: rgba(124, 58, 237, 0.08);
        transform: translateY(-12px) scale(1.03) rotateX(5deg);
        border-color: var(--accent-vibrant);
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
    }}

    .metric-value {{
        font-size: 4rem;
        font-weight: 900;
        color: var(--text-primary);
        font-family: 'Outfit', sans-serif;
        line-height: 1;
        margin-bottom: 0.8rem;
        background: var(--title-gradient);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }}

    .metric-label {{
        font-size: 0.75rem;
        color: var(--sub-text);
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 0.18em;
    }}

    .divider {{
        height: 1px;
        background: linear-gradient(to right, transparent, var(--accent), transparent);
        opacity: 0.2;
        margin: 5rem 0;
    }}

    /* Form UI Upgrade */
    .stNumberInput input, .stSelectbox [data-baseweb="select"] {{
        background: var(--input-bg) !important;
        color: var(--text-primary) !important;
        border-radius: 16px !important;
        border: 2px solid var(--card-border) !important;
        padding: 0.6rem !important;
        font-weight: 600 !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }}

    .stNumberInput input:focus, .stSelectbox [data-baseweb="select"]:focus-within {{
        border-color: var(--accent-vibrant) !important;
        box-shadow: 0 0 20px rgba(6, 182, 212, 0.3) !important;
        background: var(--card-bg) !important;
        transform: scale(1.01);
    }}
    
    label p {{
        font-size: 0.8rem !important;
        font-weight: 800 !important;
        color: var(--text-primary) !important;
        text-transform: uppercase !important;
        letter-spacing: 0.1em !important;
        margin-bottom: 0.5rem !important;
    }}

    /* Animations */
    @keyframes hyperReveal {{
        0% {{ opacity: 0; transform: translateY(60px) scale(0.95) perspective(1000px) rotateX(10deg); filter: blur(20px); }}
        100% {{ opacity: 1; transform: translateY(0) scale(1) perspective(1000px) rotateX(0deg); filter: blur(0); }}
    }}
    @keyframes pulseGlow {{
        0% {{ box-shadow: 0 0 0 0 rgba(6, 182, 212, 0.4); }}
        70% {{ box-shadow: 0 0 0 15px rgba(6, 182, 212, 0); }}
        100% {{ box-shadow: 0 0 0 0 rgba(6, 182, 212, 0); }}
    }}
    .animate-reveal {{
        animation: hyperReveal 1.4s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }}
    .pulse-btn button {{
        animation: pulseGlow 2s infinite;
    }}

    /* Disclaimer Styling */
    .disclaimer-box {{
        background: rgba(124, 58, 237, 0.1);
        border-left: 5px solid var(--accent-vibrant);
        padding: 1.8rem;
        border-radius: 0 20px 20px 0;
        margin-top: 2.5rem;
        font-size: 0.85rem;
        color: var(--sub-text);
        line-height: 1.8;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="animate-reveal">', unsafe_allow_html=True)
st.markdown('<div class="app-title">CardioSentinel</div>', unsafe_allow_html=True)
st.markdown('<div class="app-subtitle-premium">Simple Heart Health Prediction for Everyone</div>', unsafe_allow_html=True)

# ---------------- HYPER-NAVBAR ---------------- #
# This columns block is targeted by CSS to be the sticky bar
# Expanding the last col slightly to accommodate text
nav_cols = st.columns([1, 1, 1, 1, 1, 1.3])

with nav_cols[0]:
    if st.button("DASHBOARD", use_container_width=True,
                 type="primary" if st.session_state.current_page == "DASHBOARD" else "secondary"):
        nav_to("DASHBOARD")
        st.rerun()

with nav_cols[1]:
    if st.button("ASSESSMENT", use_container_width=True,
                 type="primary" if st.session_state.current_page == "PREDICTION" else "secondary"):
        nav_to("PREDICTION")
        st.rerun()

with nav_cols[2]:
    if st.button("ANALYTICS", use_container_width=True,
                 type="primary" if st.session_state.current_page == "ANALYSIS" else "secondary"):
        nav_to("ANALYSIS")
        st.rerun()

with nav_cols[3]:
    if st.button("GUIDELINES", use_container_width=True,
                 type="primary" if st.session_state.current_page == "GUIDELINES" else "secondary"):
        nav_to("GUIDELINES")
        st.rerun()

with nav_cols[4]:
    if st.button("PROTOCOL", use_container_width=True,
                 type="primary" if st.session_state.current_page == "ABOUT" else "secondary"):
        nav_to("ABOUT")
        st.rerun()

# 🌗 THEME TOGGLE (same navbar position)
with nav_cols[5]:
    # Determine button label based on CURRENT theme (allow switching to OTHER)
    theme_btn_label = "CHANGE THEME"
    
    if st.button(theme_btn_label, use_container_width=True):
        toggle_theme()
        st.rerun()



# ---------------- MODEL LOADING ---------------- #
@st.cache_resource
def load_model():
    df = pd.read_csv("Data/preprocessed_data.csv")

    FEATURE_COLUMNS = df.drop("cardio", axis=1).columns.tolist()
    SCALE_COLS = ['height', 'weight', 'ap_hi', 'ap_lo', 'BMI']

    X = df[FEATURE_COLUMNS].values
    y = df["cardio"].values

    model = LogisticRegression(max_iter=1000)
    model.fit(X, y)

    scaler = joblib.load("scaler.pkl")

    return model, FEATURE_COLUMNS, SCALE_COLS, scaler

model, FEATURE_COLUMNS, SCALE_COLS, scaler = load_model()

# ======================================================
# 📊 DASHBOARD PAGE
# ======================================================
if st.session_state.current_page == "DASHBOARD":
    # Hero Section
    st.markdown(
        """
        <div style="text-align:center; margin-bottom: 4rem;">
            <p style="color:var(--sub-text); max-width: 850px; margin: 0 auto 3rem auto; line-height: 2; font-size: 1.2rem; font-weight: 500;">
                CardioSentinel uses smart technology to check your heart health. 
                We analyze your health data to give you simple and useful insights, helping you take better care of your heart.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown('<div style="display: flex; justify-content: center; margin-bottom: 5rem;">', unsafe_allow_html=True)
    if st.button("🚀 CHECK MY HEART HEALTH", type="primary"):
        nav_to("PREDICTION")
        st.rerun()

    # Project Insights
    insight_cols = st.columns(4)
    with insight_cols[0]:
        st.markdown('<div class="metric-card"><div class="metric-value">70K+</div><div class="metric-label">Patient Records</div></div>', unsafe_allow_html=True)
    with insight_cols[1]:
        st.markdown('<div class="metric-card"><div class="metric-value">12</div><div class="metric-label">Health Factors</div></div>', unsafe_allow_html=True)
    with insight_cols[2]:
        st.markdown('<div class="metric-card"><div class="metric-value">73%</div><div class="metric-label">Prediction confidence</div></div>', unsafe_allow_html=True)
    with insight_cols[3]:
        st.markdown('<div class="metric-card"><div class="metric-value">0.71</div><div class="metric-label">Precision F1</div></div>', unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)


    # Visualizations
    col_left, col_right = st.columns(2)
    with col_left:
        st.subheader("📈 Risk Trends")
        chart_data = pd.DataFrame(np.random.randn(25, 1).cumsum(), columns=['Index'])
        st.line_chart(chart_data)
    with col_right:
        st.subheader("🎯 Model Fidelity Analysis")
        importance_data = pd.DataFrame({'Metric': ['Prec', 'Rec', 'F1', 'Acc'], 'Index': [0.72, 0.74, 0.73, 0.71]}).set_index('Metric')
        st.bar_chart(importance_data)

    st.markdown('</div>', unsafe_allow_html=True)

# ======================================================
# 🔍 ASSESSMENT PAGE (PREDICTION)
# ======================================================
elif st.session_state.current_page == "PREDICTION":
    st.markdown('<div class="animate-reveal">', unsafe_allow_html=True)
    st.markdown('<div class="app-title">Assessment Suite</div>', unsafe_allow_html=True)
    st.markdown('<div class="app-subtitle-premium">Check Your Heart Health Score</div>', unsafe_allow_html=True)

    with st.container():
        st.subheader("📋 Enter Your Details")
        
        with st.form("assessment_form_v5", clear_on_submit=False):
            st.markdown('<p style="color:#8b5cf6; font-weight:800; font-size:0.8rem; letter-spacing:0.2em; margin-bottom:1.5rem; text-transform:uppercase;">01 | Basic Info</p>', unsafe_allow_html=True)
            b_col = st.columns(3)
            gender = b_col[0].selectbox("Gender Identification", ["Female", "Male"])
            age = b_col[1].number_input("Chronological Age", 1, 120, 30)
            height = b_col[2].number_input("Height (cm)", 100, 250, 165)

            b_col2 = st.columns(3)
            weight = b_col2[0].number_input("Weight (kg)", 30, 200, 70)
            ap_hi = b_col2[1].number_input("Systolic (Upper)", 70, 250, 120)
            ap_lo = b_col2[2].number_input("Diastolic (Lower)", 40, 200, 80)

            st.markdown('<br><p style="color:#8b5cf6; font-weight:800; font-size:0.8rem; letter-spacing:0.2em; margin-bottom:1.5rem; text-transform:uppercase;">02 | Health Levels</p>', unsafe_allow_html=True)
            c_col = st.columns(2)
            cholesterol = c_col[0].selectbox("Lipid Concentration", [1, 2, 3], format_func=lambda x: ["Normal", "Elevated", "Critical"][x-1])
            gluc = c_col[1].selectbox("Glucose Saturation", [1, 2, 3], format_func=lambda x: ["Normal", "Elevated", "Critical"][x-1])

            st.markdown('<br><p style="color:#8b5cf6; font-weight:800; font-size:0.8rem; letter-spacing:0.2em; margin-bottom:1.5rem; text-transform:uppercase;">03 | Lifestyle</p>', unsafe_allow_html=True)
            l_col = st.columns(3)
            smoke = l_col[0].radio("Do you smoke?", [0, 1], format_func=lambda x: "Yes" if x else "No", horizontal=True)
            alco = l_col[1].radio("Alcohol Intake", [0, 1], format_func=lambda x: "Yes" if x else "No", horizontal=True)
            active = l_col[2].radio("Physical Activity", [0, 1], format_func=lambda x: "Regular" if x else "Low", horizontal=True)

            st.markdown("<br><br>", unsafe_allow_html=True)
            st.markdown('<div class="pulse-btn">', unsafe_allow_html=True)
            submit = st.form_submit_button("⚡ CHECK MY RISK SCORE", use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    if submit:
        # Logistic Logic
        gender_val = 1 if gender == "Male" else 0
        bmi = weight / ((height / 100) ** 2)
        input_data = {"age_years": age, "gender": gender_val, "height": height, "weight": weight, "ap_hi": ap_hi, "ap_lo": ap_lo, "cholesterol": cholesterol, "gluc": gluc, "smoke": smoke, "alco": alco, "active": active, "BMI": bmi}
        user_df = pd.DataFrame([input_data])
        user_df[SCALE_COLS] = scaler.transform(user_df[SCALE_COLS])
        user_data = user_df[FEATURE_COLUMNS].values
        probability = model.predict_proba(user_data)[0][1] * 100

        st.subheader("🛰️ Your Health Report")
        
        # --- RISK LABEL ---
        risk_label = "HIGH RISK" if probability >= 50 else "LOW RISK"
        risk_color = "#ef4444" if probability >= 50 else "#10b981"
        
        st.markdown(
            f"""
            <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 3rem 0;">
                <div style="text-align: center;">
                    <span style="font-size: 5rem; font-weight: 900; color: {risk_color}; font-family: 'Outfit'; line-height: 1; text-shadow: 0 0 30px {risk_color}40;">{risk_label}</span>
                    <p style="color: var(--sub-text); font-weight: 700; letter-spacing: 0.4em; margin-top: 1.5rem; text-transform: uppercase; font-size: 0.9rem;">Prediction Assessment</p>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        if probability >= 50:
            st.toast("⚠️ Health Warning: High Risk Detected", icon="⚠️")
            st.markdown(
                """
                <div style="background: rgba(239, 68, 68, 0.1); border-left: 5px solid #ef4444; padding: 20px; border-radius: 12px; display: flex; align-items: center; gap: 15px; margin-bottom: 2rem;">
                    <span style="font-size: 2rem;">⚠️</span>
                    <div>
                        <h4 style="color: #ef4444; margin: 0; font-size: 1.1rem; font-weight: 700;">Action Required</h4>
                        <p style="color: var(--text-primary); margin: 5px 0 0 0; font-size: 0.95rem;">
                            Your results indicate potential risk factors. We strongly recommend consulting a healthcare professional for a comprehensive check-up.
                        </p>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.toast("🎉 Great Job! Low Risk", icon="✅")
            st.balloons()
            st.markdown(
                """
                <div style="background: rgba(16, 185, 129, 0.1); border-left: 5px solid #10b981; padding: 20px; border-radius: 12px; display: flex; align-items: center; gap: 15px; margin-bottom: 2rem;">
                    <span style="font-size: 2rem;">🎉</span>
                    <div>
                        <h4 style="color: #10b981; margin: 0; font-size: 1.1rem; font-weight: 700;">Excellent Result</h4>
                        <p style="color: var(--text-primary); margin: 5px 0 0 0; font-size: 0.95rem;">
                            Your heart health markers are stable. Maintain your current healthy lifestyle and activity levels!
                        </p>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        # --- PERSONALIZED ADVICE ---
        st.markdown('<br><h5 style="color:var(--accent);">💡 Personalized Advice</h5>', unsafe_allow_html=True)
        suggestions = []
        if smoke == 1:
            suggestions.append("🚭 **Stop Smoking**: Quitting smoking is the best thing you can do for your heart.")
        if alco == 1:
            suggestions.append("🍷 **Limit Alcohol**: Reducing alcohol helps lower blood pressure.")
        if active == 0:
            suggestions.append("🏃 **Get Moving**: Try to walk for at least 30 minutes every day.")
        if bmi > 25:
            suggestions.append("⚖️ **Watch Your Weight**: A healthy weight reduces strain on your heart.")
        if ap_hi > 130 or ap_lo > 80:
            suggestions.append("💓 **Check Blood Pressure**: Your numbers are a bit high. Monitor them regularly.")
        if cholesterol > 1:
            suggestions.append("🍔 **Eat Healthy Fats**: Avoid fried foods to lower your cholesterol.")
        if gluc > 1:
            suggestions.append("🍭 **Watch Sugar Intake**: High sugar can damage blood vessels.")
        
        if len(suggestions) > 0:
            for s in suggestions:
                st.markdown(f"<div style='background:rgba(255,255,255,0.05); padding:10px 15px; border-radius:10px; margin-bottom:10px; border-left: 3px solid var(--accent); color:var(--text-primary);'>{s}</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div style='background:rgba(255,255,255,0.05); padding:10px 15px; border-radius:10px; margin-bottom:10px; border-left: 3px solid #10b981; color:var(--text-primary);'>✨ You are doing everything right! Keep it up!</div>", unsafe_allow_html=True)

        st.markdown(
            """
            <div class="disclaimer-box">
                <b>Note:</b> This result is just an estimate based on your data. It is 73% accurate but 
                <b>this is not a medical diagnosis</b>. Please consult a doctor for a real medical check-up.
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown('</div>', unsafe_allow_html=True)

# ======================================================
# 📈 ANALYTICS PAGE
# ======================================================
elif st.session_state.current_page == "ANALYSIS":
    import analysis
    analysis.show_analysis()

# ======================================================
# 🥗 GUIDELINES PAGE
# ======================================================
elif st.session_state.current_page == "GUIDELINES":
    import guidelines
    guidelines.show_guidelines()

# ======================================================
# ℹ️ PROTOCOL PAGE (ABOUT)
# ======================================================
elif st.session_state.current_page == "ABOUT":
    import about
    about.show_about()

# ======================================================
# 💰 PRICELIST MODAL (SIMULATED)
# ======================================================
if "show_pricelist" in st.session_state and st.session_state.show_pricelist:
    st.subheader("💰 Service Quotation & Pricelist")
    
    col_p1, col_p2 = st.columns(2)
    with col_p1:
        st.write("**Diagnostics Services**")
        st.write("- Basic Heart Screening: $49")
        st.write("- Advanced Cardiovascular Profiling: $120")
        st.write("- Consultative AI Analysis: $25")
    
    with col_p2:
        st.write("**Preventive Plans**")
        st.write("- Monthly Monitoring: $15/mo")
        st.write("- Personalized Health Coach: $80/mo")
    
    st.markdown("---")
    st.write("### Request a Detailed Quotation")
    with st.form("pricelist_form"):
        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        service = st.multiselect("Select Services", ["Basic Screening", "Advanced Profiling", "Monthly Monitoring"])
        
        submitted_quote = st.form_submit_button("Submit Request")
        if submitted_quote:
            st.success(f"Thank you {name}! Your quotation request has been sent to {email}.")
    
    if st.button("Close Pricelist"):
        st.session_state.show_pricelist = False
        st.rerun()
