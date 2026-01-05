import streamlit as st
import pandas as pd

def show_analysis():
    st.markdown('<div class="app-subtitle-premium">Understanding Your Risk Score</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <div class="card">
            <h4 style="color:var(--accent);">📌 Risk Levels</h4>
            <ul style="color:var(--text-primary); list-style-type: none; padding-left: 0; line-height: 2.2; font-size: 0.95rem;">
                <li><span style="color:#10b981;">🟢</span> <b>GOOD / LOW RISK</b> &rarr; 0–30%</li>
                <li><span style="color:#f59e0b;">🟡</span> <b>MEDIUM RISK / BE CAREFUL</b> &rarr; 30–60%</li>
                <li><span style="color:#ef4444;">🔴</span> <b>HIGH RISK / SEE A DOCTOR</b> &rarr; 60%+</li>
            </ul>
            <p style="color:var(--sub-text); font-size: 0.8rem; margin-top: 1rem; font-style: italic;">
                These levels show how likely it is to have a heart issue based on data from many people.
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class="card">
            <h4 style="color:var(--accent);">🧪 How We Test</h4>
            <p style="color:var(--sub-text); line-height:1.8; font-size: 0.95rem;">
            Our <b>Smart Engine</b> uses math to check your health details. 
            By comparing your data with 70,000 other records, we can find important patterns.
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown('<h4 style="color:var(--accent);">📊 What Affects Your Score?</h4>', unsafe_allow_html=True)
    st.markdown(
        """
        <p style="color:var(--sub-text); line-height:1.8; margin-bottom: 2rem;">
        The system looks at different things to calculate your risk. 
        Below is a list of what matters most:
        </p>
        """,
        unsafe_allow_html=True
    )
    
    weights = {
        'Systolic Pressure (Top Number)': '0.42 (Most Important)',
        'Diastolic Pressure (Bottom Number)': '0.28 (Very Important)',
        'Age': '0.15 (Important)',
        'Cholesterol Levels': '0.10 (Factor)',
        'BMI (Body Mass)': '0.05 (Factor)'
    }
    
    for key, val in weights.items():
        st.markdown(f"""
        <div style="display:flex; justify-content:space-between; padding: 1rem 0; border-bottom: 1px solid var(--card-border);">
            <span style="color:var(--text-primary); font-weight:700;">{key}</span>
            <span style="color:var(--accent-vibrant); font-family:'Outfit'; font-weight:800;">{val}</span>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<h4 style="color:var(--accent);">🔬 What We Found</h4>', unsafe_allow_html=True)
    st.markdown(
        """
        <p style="color:var(--sub-text); line-height:1.8;">
        Checking 70,000 records showed that older age and high blood pressure significantly increase risk. 
        Our system filters out small changes like simple weight differences to focus on what really hurts your heart. 
        This is why our system is 73% accurate.
        </p>
        """,
        unsafe_allow_html=True
    )
    st.markdown('</div>', unsafe_allow_html=True)
