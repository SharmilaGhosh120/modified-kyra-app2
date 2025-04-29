
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set page configuration
st.set_page_config(page_title="Ky'ra Internship Dashboard", layout="wide")

# -------------------------
# Session Initialization
# -------------------------
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False
    st.session_state["role"] = None

# -------------------------
# Login Page
# -------------------------
def login():
    st.title("Ky'ra Internship Dashboard Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    roles = ["Student", "College", "Mentor", "MSME", "Government"]
    role = st.selectbox("Select your role", roles)

    if st.button("Login"):
        if email and password:
            st.session_state["authenticated"] = True
            st.session_state["role"] = role
            st.success(f"Welcome {role}!")
        else:
            st.error("Please enter valid credentials.")

# -------------------------
# Navigation Sidebar
# -------------------------
def sidebar_menu():
    return st.sidebar.radio("📌 Navigation", ["Dashboard", "Register", "FAQ", "Logout"])

# -------------------------
# Role-Based Dashboards
# -------------------------
@st.cache_data
def get_sample_data():
    return pd.DataFrame({
        'Month': ['Jan', 'Feb', 'Mar'],
        'Internships': [1, 2, 3]
    })

def show_dashboard(role):
    st.title(f"{role} Dashboard")

    data = get_sample_data()

    if role == "Student":
        st.subheader("Internship Progress")
        st.line_chart(data.set_index("Month"))

    elif role == "College":
        st.subheader("Students Overview")
        st.bar_chart(data.set_index("Month"))

    elif role == "Mentor":
        st.subheader("Mentor Feedback Overview")
        st.area_chart(data.set_index("Month"))

    elif role == "MSME":
        st.subheader("Posted Internships")
        st.dataframe(data)

    elif role == "Government":
        st.subheader("Government Schemes Overview")
        st.pyplot(get_government_pie_chart())

def get_government_pie_chart():
    fig, ax = plt.subplots()
    ax.pie([30, 40, 30], labels=['Skilling', 'MSME', 'Women Empowerment'], autopct='%1.1f%%')
    return fig

# -------------------------
# Registration Forms
# -------------------------
def show_registration_form(role):
    st.title(f"{role} Registration Form")

    with st.form(f"{role.lower()}_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone")
        
        if role == "Student":
            college = st.text_input("College")
            course = st.text_input("Course")
            semester = st.text_input("Semester")
        elif role == "College":
            college_name = st.text_input("College Name")
            coordinator = st.text_input("Coordinator Name")
        elif role == "Mentor":
            domain = st.text_input("Domain Expertise")
        elif role == "MSME":
            company = st.text_input("Company Name")
            industry = st.text_input("Industry Type")
        elif role == "Government":
            dept = st.text_input("Department")
            designation = st.text_input("Designation")

        submitted = st.form_submit_button("Submit")
        if submitted:
            st.success("Form submitted successfully!")

# -------------------------
# FAQ Section
# -------------------------
def show_faq():
    st.title("❓ Frequently Asked Questions")

    faq = {
        "How to register?": "Go to the 'Register' tab and fill out the form based on your role.",
        "How to apply for internships?": "Students can go to their dashboard and click on available internships.",
        "How do MSMEs post internships?": "MSME users can post internship details from their dashboard.",
        "Where do I provide feedback?": "Mentors can provide feedback via their dashboard section.",
    }

    question = st.selectbox("Choose a question:", list(faq.keys()))
    st.markdown(f"**Answer:** {faq[question]}")

# -------------------------
# Logout Handler
# -------------------------
def logout():
    st.session_state["authenticated"] = False
    st.session_state["role"] = None
    st.success("You have been logged out.")
    st.experimental_rerun()

# -------------------------
# Main App Logic
# -------------------------
def main():
    if not st.session_state["authenticated"]:
        login()
    else:
        role = st.session_state["role"]
        choice = sidebar_menu()

        if choice == "Dashboard":
            show_dashboard(role)
        elif choice == "Register":
            show_registration_form(role)
        elif choice == "FAQ":
            show_faq()
        elif choice == "Logout":
            logout()

# -------------------------
# Run App
# -------------------------
if __name__ == "__main__":
    main()
