import streamlit as st
st.set_page_config(
    page_title="Student Guide | EduPredict",
    page_icon="📚",
    layout="wide"
)
col1, col2 = st.columns([1, 6])
with col1:
    if st.button("🏠 Home", use_container_width=True,key="home2"):
        st.switch_page("app.py")
with col2:
    st.title("📚 Student Success Guide")
    st.caption("Simple and practical tips to improve academic performance.")
st.divider()
st.subheader("📖 Effective Study Tips")
col1, col2 = st.columns(2)
with col1:
    st.info("""
### 📚 Study Every Day
- Study consistently instead of only before exams.
- Revise previous topics daily.
- Take a short break after every 45–60 minutes.
- Avoid last-minute preparation.
""")
with col2:
    st.info("""
### 🧠 Active Learning
- Make handwritten notes.
- Teach concepts to a friend.
- Solve previous year question papers.
- Practice regularly.
""")
st.divider()
st.subheader("⏰ Time Management")
col1, col2 = st.columns(2)
with col1:
    st.success("""
### 🌅 Daily Routine
**Morning**
- Revise difficult subjects
**Afternoon**
- Complete assignments
**Evening**
- Practice numerical problems
""")
with col2:
    st.success("""
### 📅 Weekly Goals
✅ Complete class notes
✅ Revise every subject
✅ Attempt one mock test
✅ Analyze mistakes
""")
st.divider()
# EXAM PREPARATION
st.subheader("📝 Exam Preparation")
st.warning("""
- Start preparation at least 3–4 weeks before exams.
- Focus more on weak subjects.
- Solve sample papers regularly.
- Manage your time during the examination.
- Avoid learning completely new topics one day before exams.
""")
st.divider()
st.subheader("💪 Healthy Study Habits")
c1, c2, c3 = st.columns(3)
with c1:
    st.success("""
### 💤 Sleep
Get 7–8 hours of sleep every day for better concentration.
""")
with c2:
    st.success("""
### 🥗 Healthy Diet
Eat nutritious food and drink enough water while studying.
""")
with c3:
    st.success("""
### 🚶 Exercise
Exercise for 20–30 minutes daily to reduce stress.
""")
st.divider()
st.subheader("🧠 Memory Techniques")
st.info("""
Try these learning techniques:
- 📌 Spaced Repetition
- 📌 Active Recall
- 📌 Mind Mapping
- 📌 Flashcards
- 📌 Pomodoro Technique
- 📌 Practice Tests
""")
st.divider()
st.subheader("🎯 Daily Motivation")
st.success("""
> **Success is the result of small efforts repeated every day.**
Stay consistent, believe in yourself, and keep learning.
""")
st.divider()
st.subheader("✅ Daily Study Checklist")
st.checkbox("📖 Studied today's topics")
st.checkbox("📝 Revised previous lectures")
st.checkbox("📚 Solved practice questions")
st.checkbox("📋 Completed assignments")
st.checkbox("⏳ Studied for at least one hour")
st.checkbox("💤 Slept for 7–8 hours")
st.divider()
st.subheader("🚀 Quick Navigation")
c1, c2, c3 = st.columns(3)
with c1:
    if st.button("🎯 Prediction", use_container_width=True):
        st.switch_page("pages/1_Prediction.py")
with c2:
    if st.button("❓ Help", use_container_width=True):
        st.switch_page("pages/4_Help.py")
with c3:
    if st.button("🏠 Home", use_container_width=True,key="home1"):
        st.switch_page("app.py")
st.divider()
st.caption("© EduPredict | Student Success Guide")