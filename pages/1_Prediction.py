import streamlit as st
import pandas as pd
import joblib
st.set_page_config(
    page_title="Prediction | EduPredict",
    page_icon="🎓",
    layout="wide"
)
model = joblib.load("model/student_model.pkl")
col1, col2 = st.columns([1, 6])
with col1:
    if st.button("🏠 Home", use_container_width=True):
        st.switch_page("app.py")
with col2:
    st.title("🎓 Student Performance Prediction")
    st.caption("Predict a student's final examination marks using Artificial Intelligence.")
st.divider()
st.subheader("📝 Student Details")
with st.form("prediction_form"):
    col1, col2 = st.columns(2)
    with col1:
        student_name = st.text_input(
            "👤 Student Name"
        )
        study_hours = st.slider(
            "📚 Study Hours",
            min_value=1,
            max_value=4,
            value=2
        )
        attendance = st.slider(
            "🏫 Attendance (%)",
            min_value=0,
            max_value=100,
            value=75
        )
    with col2:
        first_marks = st.number_input(
            "📝 First Sessional Marks (Out of 20)",
            min_value=0,
            max_value=20,
            value=10
        )
        second_marks = st.number_input(
            "📖 Second Sessional Marks (Out of 20)",
            min_value=0,
            max_value=20,
            value=10
        )

    predict = st.form_submit_button(
        "🚀 Predict Performance",
        use_container_width=True
    )
if predict:
    if student_name.strip() == "":
        st.error("Please enter the student's name.")
    else:
        input_df = pd.DataFrame({
            "StudyHours": [study_hours],
            "Attendance": [attendance],
            "FirstSessionalMarks": [first_marks],
            "SecondSessionalMarks": [second_marks]
        })
        prediction = model.predict(input_df)[0]
        prediction = round(prediction, 2)
        prediction = max(0, min(100, prediction))
        if prediction >= 90:
            grade = "A+"
            performance = "Outstanding"
        elif prediction >= 80:
            grade = "A"
            performance = "Excellent"
        elif prediction >= 70:
            grade = "B"
            performance = "Very Good"
        elif prediction >= 60:
            grade = "C"
            performance = "Good"
        elif prediction >= 50:
            grade = "D"
            performance = "Average"
        else:
            grade = "F"
            performance = "Needs Improvement"
        confidence = min(
            99,
            round(
                75 +
                attendance * 0.08 +
                study_hours * 2
            )
        )
        st.divider()
        st.subheader("📊 Prediction Result")
        c1, c2, c3 = st.columns(3)
        with c1:
            st.metric("🎯 Predicted Marks", f"{prediction}/100")
        with c2:
            st.metric("🏅 Grade", grade)
        with c3:
            st.metric("📈 Performance", performance)
        if prediction >= 40:
            st.success("✅ Result: PASS")
        else:
            st.error("❌ Result: FAIL")
        st.write(f"### Prediction Confidence: {confidence}%")
        st.progress(confidence / 100)
        st.divider()
        st.subheader("💡 Personalized Suggestions")
        suggestions = []
        if attendance < 75:
            suggestions.append("Improve your attendance to at least 75%.")
        if study_hours <= 1:
            suggestions.append("Increase your daily study hours.")
        if first_marks < 10:
            suggestions.append("Revise topics covered in the First Sessional.")
        if second_marks < 10:
            suggestions.append("Focus more on the Second Sessional subjects.")
        if prediction >= 85:
            suggestions.append("Excellent performance. Keep maintaining your consistency.")
        elif prediction >= 70:
            suggestions.append("Good work. Continue regular practice.")
        elif prediction >= 50:
            suggestions.append("Spend more time revising and solving previous year papers.")
        else:
            suggestions.append("Prepare a proper study timetable and seek guidance from teachers.")
        for item in suggestions:
            st.success(item)
        st.divider()
        st.subheader("📋 Performance Summary")
        summary = pd.DataFrame({
            "Parameter": [
                "Student Name",
                "Study Hours",
                "Attendance",
                "First Sessional Marks",
                "Second Sessional Marks",
                "Predicted Marks",
                "Grade",
                "Performance"
            ],
            "Value": [
                student_name,
                study_hours,
                f"{attendance}%",
                first_marks,
                second_marks,
                f"{prediction}/100",
                grade,
                performance
            ]
        })
        st.table(summary)
        st.divider()
        st.balloons()
        st.success("Prediction completed successfully!")
else:
    st.info("Fill in the student details above and click **Predict Performance**.")