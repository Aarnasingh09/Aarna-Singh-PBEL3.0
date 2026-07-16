import streamlit as st
st.set_page_config(
    page_title="EduPredict",
    page_icon="🎓",
    layout="wide"
)
col1, col2 = st.columns([1, 5])
with col1:
    st.image("images/logo.png", width=90)
with col2:
    st.title("EduPredicts")
    st.caption("AI-Driven Student Performance Prediction")
st.divider()
left, right = st.columns([1.3, 1])
with left:
    st.title("Predict Student Performance with AI")
    st.write("""
EduPredict is an AI-powered web application that predicts a student's
final examination marks using Machine Learning.
The prediction is based on:
- 📚 Study Hours
- 🏫 Attendance
- 📝 First Sessional Marks
- 📖 Second Sessional Marks
Get instant predictions along with personalized suggestions to improve academic performance.
""")
    if st.button("🚀 Get Started"):
        st.switch_page("pages/1_Prediction.py")
with right:
    st.image("images/hero.png", use_container_width=True)
st.divider()
st.subheader("Why Choose EduPredict?")
c1, c2, c3 = st.columns(3)
with c1:
    st.info("""
### 🤖 AI Prediction
Predict final marks using a trained Random Forest Machine Learning model.
""")
with c2:
    st.success("""
### 🎯 Smart Suggestions
Receive personalized suggestions to improve academic performance.
""")
with c3:
    st.warning("""
### 📊 Accurate Results
Fast, reliable, and easy-to-understand prediction reports.
""")
st.divider()
st.subheader("Platform Highlights")
m1, m2, m3, m4 = st.columns(4)
m1.metric("Algorithm", "Random Forest")
m2.metric("Prediction", "Out of 100")
m3.metric("Input Features", "4")
m4.metric("Model", "ML Based")
st.divider()
st.subheader("Quick Access")
q1, q2, q3 = st.columns(3)
with q1:
    if st.button("🎯 Prediction", use_container_width=True):
        st.switch_page("pages/1_Prediction.py")
with q2:
    if st.button("📚 Student Guide", use_container_width=True):
        st.switch_page("pages/3_Student_Guide.py")
with q3:
    if st.button("❓ Help", use_container_width=True):
        st.switch_page("pages/4_Help.py")
st.divider()
st.subheader("About EduPredict")
st.write("""
EduPredict is an AI-based educational platform that predicts a student's expected final examination marks using Machine Learning.
The model uses four academic parameters:
- 📚 Study Hours
- 🏫 Attendance
- 📝 First Sessional Marks
- 📖 Second Sessional Marks
The goal is to help students understand their expected performance and improve before the final examination.
""")
st.divider()
st.subheader("How EduPredict Works")
a, b, c, d = st.columns(4)
a.success("1️⃣ Enter Student Details")
b.success("2️⃣ AI Processes Data")
c.success("3️⃣ Predict Final Marks")
d.success("4️⃣ Get Suggestions")
st.divider()
st.subheader("Need Help?")
st.info("""
Visit the **Help** page to learn:
- Frequently Asked Questions
- How predictions work
- Tips for better performance
- How to use EduPredict
""")
st.divider()
st.caption("© EduPredict | AI-Driven Student Performance Prediction")