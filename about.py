import streamlit as st

def show_about():
    st.markdown('<div class="app-title">About</div>', unsafe_allow_html=True)
    st.markdown(
    """
    <div style="
        text-align:center;
        margin-bottom:30px;
        font-family: 'Poppins', 'Segoe UI', sans-serif;
        letter-spacing: 0.6px;
    ">
        <span style="
            font-size:0.9rem;
            color:var(--sub-text);
        ">Developed by</span><br>
        <span style="
            font-size:1.4rem;
            font-weight:800;
            background: linear-gradient(90deg, var(--accent), var(--accent-vibrant));
            -webkit-background-clip:text;
            -webkit-text-fill-color:transparent;
        ">
            Dhruvi Valera
        </span>
    </div>
    """,
    unsafe_allow_html=True
)

    st.markdown('<div class="app-subtitle-premium">How It Works</div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="card">
        <h4 style="color:var(--accent);">⚙️ Model Accuracy</h4>
        <div style="display: flex; gap: 12px; flex-wrap: wrap; margin-top: 15px; margin-bottom: 30px;">
            <div style="background: rgba(124, 58, 237, 0.1); border: 1px solid var(--accent); padding: 8px 24px; border-radius: 50px; color: var(--text-primary); font-weight: 700; font-size: 0.8rem;">73.0% Accuracy</div>
            <div style="background: rgba(124, 58, 237, 0.1); border: 1px solid var(--accent); padding: 8px 24px; border-radius: 50px; color: var(--text-primary); font-weight: 700; font-size: 0.8rem;">Smart Analysis</div>
            <div style="background: rgba(124, 58, 237, 0.1); border: 1px solid var(--accent); padding: 8px 24px; border-radius: 50px; color: var(--text-primary); font-weight: 700; font-size: 0.8rem;">Advanced Math</div>
        </div>

        <h4 style="color:var(--accent);">🚀 System Info</h4>
        <p style="color:var(--sub-text); line-height:1.9; font-size: 1rem;">
        HeartCare AI uses a <b>Python Code</b> to check your health data. Unlike other complex systems, our code is clear and 
        uses standard math to understand the risk, so we know exactly how it works.
        </p>
        <div style="background:rgba(0,0,0,0.2); padding:1rem; border-radius:10px; font-family:monospace; color:var(--accent-vibrant); font-size:0.85rem; margin:1.5rem 0;">
            h(x) = σ(θᵀx) = 1 / (1 + e⁻ᶿᵀˣ)
        </div>
        
        <h4 style="color:var(--accent); margin-top:30px;">🛰️ Version History</h4>
        <table style="width:100%; border-collapse:collapse; margin-top:10px;">
            <tr style="border-bottom:1px solid var(--card-border);">
                <td style="padding:10px; color:var(--text-primary);"><b>v1.0</b></td>
                <td style="padding:10px; color:var(--sub-text);">Baseline Scalar Regression</td>
            </tr>
            <tr style="border-bottom:1px solid var(--card-border);">
                <td style="padding:10px; color:var(--text-primary);"><b>v2.0</b></td>
                <td style="padding:10px; color:var(--sub-text);">Multi-Vector Neural Mapping</td>
            </tr>
            <tr style="border-bottom:1px solid var(--card-border);">
                <td style="padding:10px; color:var(--text-primary);"><b>v2.1</b></td>
                <td style="padding:10px; color:var(--accent-vibrant);">Hyper-Vibrant UI & High-Fidelity Logic</td>
            </tr>
        </table>

        <h4 style="color:var(--accent); margin-top:40px;">⚠️ Important Note</h4>
        <p style="color:var(--sub-text); font-size:0.9rem; font-style: italic; line-height: 1.7; opacity: 0.8;">
        All results are just estimates. This tool helps you see your risk, 
        but it does not replace a real doctor. Please see a cardiologist for a real check-up.
        </p>
        </div>
        """,
        unsafe_allow_html=True
    )
