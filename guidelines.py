import streamlit as st

def show_guidelines():
    st.markdown('<div class="app-title">Health Guidelines</div>', unsafe_allow_html=True)
    st.markdown('<div class="app-subtitle-premium">Simple Tips for a Healthy Life</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <div class="card">
            <h4 style="color:var(--accent);">🥗 Diet & Nutrition</h4>
            <p style="color:var(--sub-text); line-height:1.8; font-size: 0.95rem;">
            A good diet keeps your heart strong. Eat foods with lots of fiber and good nutrients to keep your blood vessels healthy.
            </p>
            <ul style="color:var(--text-primary); list-style-type: none; padding-left: 0; line-height: 2.2; font-size: 0.9rem;">
                <li>✅ <b>Omega-3 fats</b> &rarr; Good for heart repair</li>
                <li>✅ <b>healthy carbs</b> &rarr; Stable energy</li>
                <li>❌ <b>Bad Fats (Trans fats)</b> &rarr; Clogs arteries</li>
            </ul>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class="card">
            <h4 style="color:var(--accent);">⚡ Exercise Routine</h4>
            <p style="color:var(--sub-text); line-height:1.8; font-size: 0.95rem;">
            Moving your body helps your heart pump better. Try to get 150 minutes of moderate exercise (like brisk walking) every week.
            </p>
             <ul style="color:var(--text-primary); list-style-type: none; padding-left: 0; line-height: 2.2; font-size: 0.9rem;">
                <li>🏃 <b>Cardio / Running</b> &rarr; Stronger heart</li>
                <li>🧘 <b>Relaxation / Yoga</b> &rarr; Less stress</li>
                <li>💤 <b>Rest & Sleep</b> &rarr; Body repair</li>
            </ul>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown('<h4 style="color:var(--accent);">🩺 Managing High Blood Pressure</h4>', unsafe_allow_html=True)
    st.markdown(
        """
        <p style="color:var(--sub-text); line-height:1.8; margin-bottom: 1.5rem;">
        If your risk is <b>Medium</b> or <b>High</b>, lowering your blood pressure is key. 
        Here is how you can do it:
        </p>
        <div style="background:rgba(255,255,255,0.03); padding:1.5rem; border-radius:20px; border-left:4px solid var(--accent-vibrant);">
            <p style="color:var(--text-primary); font-weight:700; margin-bottom:0.5rem;">🔹 Watch Salt and Eat Greens</p>
            <p style="color:var(--sub-text); font-size:0.9rem;">Eat less salt (sodium) and eat more leafy greens to help your blood flow better.</p>
        </div>
        <br>
        <div style="background:rgba(255,255,255,0.03); padding:1.5rem; border-radius:20px; border-left:4px solid var(--accent);">
            <p style="color:var(--text-primary); font-weight:700; margin-bottom:0.5rem;">🔹 Relax and Breathe</p>
            <p style="color:var(--sub-text); font-size:0.9rem;">Stress raises blood pressure. Try to take 10 minutes a day to just breathe and relax.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<h4 style="color:var(--accent);">🩸 Keeping Cholesterol Low</h4>', unsafe_allow_html=True)
    st.markdown(
        """
        <p style="color:var(--sub-text); line-height:1.8;">
        Cholesterol is a factor (0.10) in your risk score because it can block arteries. 
        To improve it:
        </p>
        <ul style="color:var(--text-primary); line-height:2; font-size:0.95rem;">
            <li><b>Good Cholesterol (HDL):</b> Exercise more and eat fish/nuts (Omega-3).</li>
            <li><b>Bad Cholesterol (LDL):</b> Avoid fried foods and bad oils.</li>
            <li><b>Healthy Arteries:</b> Eat fruits and vegetables (Antioxidants).</li>
        </ul>
        """,
        unsafe_allow_html=True
    )
    st.markdown('</div>', unsafe_allow_html=True)
