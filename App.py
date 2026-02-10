import streamlit as st
from datetime import date

st.set_page_config(page_title="AI Smart Study Planner", layout="wide")

st.title("📘 AI-Based Smart Study Planner")
st.subheader("For RBI | SSC | Banking | Government Exams")

st.markdown("---")

# Sidebar
st.sidebar.header("🎯 Exam Details")
exam = st.sidebar.selectbox(
    "Select Exam",
    ["RBI", "SSC", "Banking", "Other Government Exams"]
)

exam_date = st.sidebar.date_input("Exam Date", min_value=date.today())

st.sidebar.markdown("---")

# Tabs
tab1, tab2, tab3 = st.tabs(["📅 Study Planner", "📊 Performance Analysis", "📈 Progress Tracker"])

# -------- Study Planner --------
with tab1:
    st.header("Personalized Study Plan")

    if st.button("Generate Study Plan"):
        st.success(f"Study Plan Generated for {exam}")

        st.write("### Daily Study Allocation")
        st.table({
            "Subject": ["Quantitative Aptitude", "Reasoning", "English", "General Awareness"],
            "Hours/Day": ["2 hrs", "1.5 hrs", "1 hr", "1 hr"]
        })

        st.info("🔔 AI Tip: Focus more on Quant & Reasoning for higher scoring potential.")

# -------- Performance Analysis --------
with tab2:
    st.header("Weak Area Detection")

    st.write("Enter your recent mock test scores:")

    quant = st.slider("Quantitative Aptitude", 0, 100, 50)
    reasoning = st.slider("Reasoning", 0, 100, 60)
    english = st.slider("English", 0, 100, 70)
    ga = st.slider("General Awareness", 0, 100, 40)

    if st.button("Analyze Performance"):
        st.warning("📉 Weak Subjects Identified:")

        weak_subjects = []
        if quant < 50:
            weak_subjects.append("Quantitative Aptitude")
        if reasoning < 50:
            weak_subjects.append("Reasoning")
        if english < 50:
            weak_subjects.append("English")
        if ga < 50:
            weak_subjects.append("General Awareness")

        if weak_subjects:
            for subject in weak_subjects:
                st.write(f"- {subject}")
        else:
            st.success("🎉 No weak subjects detected. Keep going!")

# -------- Progress Tracker --------
with tab3:
    st.header("Preparation Consistency")

    days_studied = st.slider("Days Studied This Week", 0, 7, 4)

    st.progress(days_studied / 7)

    if days_studied >= 5:
        st.success("🔥 Excellent consistency!")
    else:
        st.info("💡 Try to study at least 5 days a week for better results.")
