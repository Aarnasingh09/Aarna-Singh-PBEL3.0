import streamlit as st
st.set_page_config(
    page_title="Help | EduPredict",
    page_icon="❓",
    layout="wide"
)
col1, col2 = st.columns([1, 6])
with col1:
    if st.button("🏠 Home", use_container_width=True,key="home_upper"):
        st.switch_page("app.py")
with col2:
    st.title("❓ Help & Support")
    st.caption("Find answers to common questions about EduPredict.")
st.divider()
st.subheader("📌 Frequently Asked Questions")
with st.expander("What is EduPredict?"):
    st.write("""
EduPredict is an AI-powered web application that predicts a student's final examination marks using Machine Learning.
""")
with st.expander("Which Machine Learning algorithm is used?"):
    st.write("""
EduPredict uses the **Random Forest Regressor** algorithm from Scikit-learn.
""")
with st.expander("What inputs are required?"):
    st.write("""
The prediction is based on four academic factors:
- 📚 Study Hours
- 🏫 Attendance
- 📝 First Sessional Marks
- 📖 Second Sessional Marks
""")
with st.expander("How accurate is the prediction?"):
    st.write("""
The prediction is based on patterns learned from the training dataset.
It should be considered an estimate rather than an exact result.
""")
with st.expander("Are my details stored?"):
    st.write("""
No.
EduPredict does not store any student information.
Predictions are generated instantly and are not saved.
""")
st.divider()
st.subheader("🤖 How EduPredict Works")
st.info("""
### Step 1
Enter the student's academic details.
### Step 2
The trained Machine Learning model processes the data.
### Step 3
The model predicts the expected final marks.
### Step 4
EduPredict displays:
- 🎯 Predicted Marks
- 🏅 Grade
- ✅ Pass/Fail Status
- 💡 Performance Suggestions
""")
st.divider()
st.subheader("✨ Features")
col1, col2 = st.columns(2)
with col1:
    st.success("""
✔ AI-Based Prediction
✔ Personalized Suggestions
✔ Performance Summary
✔ Download Prediction Report
""")
with col2:
    st.success("""
✔ Student Guide
✔ Interactive Interface
✔ Fast Prediction
✔ Easy to Use
""")
st.divider()
st.subheader("💡 Tips for Better Predictions")
st.warning("""
- Enter the correct attendance percentage.
- Enter your actual sessional marks.
- Use realistic study hours.
- Predictions are estimates and should be used as academic guidance.
""")
st.divider()
st.subheader("🛠 Technologies Used")
t1, t2, t3 = st.columns(3)
with t1:
    st.info("""
### Programming
- Python
- Pandas
- NumPy
""")
with t2:
    st.info("""
### Machine Learning
- Scikit-learn
- Random Forest Regression
- Train-Test Split
""")
with t3:
    st.info("""
### Framework
- Streamlit
- Joblib
- Git & GitHub
""")
st.divider() 
st.subheader("🚀 Quick Navigation")
c1, c2, c3 = st.columns(3)
with c1:
    if st.button("🎯 Prediction", use_container_width=True):
        st.switch_page("pages/1_Prediction.py")
with c2:
    if st.button("📚 Student Guide", use_container_width=True):
        st.switch_page("pages/3_Student_Guide.py")
with c3:
    if st.button("🏠 Home", use_container_width=True,key="home_bottom"):
        st.switch_page("app.py")
st.divider()
st.caption("©  EduPredict | AI-Driven Student Performance Prediction")