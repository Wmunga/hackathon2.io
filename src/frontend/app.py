import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta
import requests
import json

# API configuration
API_URL = "http://localhost:8000"

# Page config
st.set_page_config(
    page_title="HealthTech Reminder System",
    page_icon="🏥",
    layout="wide"
)

# Helper functions
def get_patients():
    response = requests.get(f"{API_URL}/patients/")
    if response.status_code == 200:
        return response.json()
    return []

def create_patient(name, email, phone):
    response = requests.post(
        f"{API_URL}/patients/",
        params={"name": name, "email": email, "phone": phone}
    )
    return response.status_code == 200

def get_appointments():
    response = requests.get(f"{API_URL}/appointments/")
    if response.status_code == 200:
        return response.json()
    return []

def create_appointment(patient_id, datetime_str, type, notes=None):
    response = requests.post(
        f"{API_URL}/appointments/",
        params={
            "patient_id": patient_id,
            "datetime_str": datetime_str,
            "type": type,
            "notes": notes
        }
    )
    return response.status_code == 200

# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to",
    ["Dashboard", "Patients", "Appointments", "Settings"]
)

# Main content
st.title("🏥 HealthTech Reminder System")

if page == "Dashboard":
    st.header("Provider Dashboard")
    
    # Get data
    patients = get_patients()
    appointments = get_appointments()
    
    # Quick stats
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        today_appointments = len([a for a in appointments if datetime.fromisoformat(a["datetime"]).date() == datetime.now().date()])
        st.metric("Today's Appointments", today_appointments)
    with col2:
        pending_reminders = len([a for a in appointments if a["status"] == "scheduled"])
        st.metric("Pending Reminders", pending_reminders)
    with col3:
        completed_today = len([a for a in appointments if a["status"] == "completed" and datetime.fromisoformat(a["datetime"]).date() == datetime.now().date()])
        st.metric("Completed Today", completed_today)
    with col4:
        no_shows = len([a for a in appointments if a["status"] == "cancelled" and datetime.fromisoformat(a["datetime"]).date() == datetime.now().date()])
        st.metric("No-Shows", no_shows)
    
    # Calendar view
    st.subheader("Upcoming Appointments")
    if appointments:
        df = pd.DataFrame(appointments)
        df["datetime"] = pd.to_datetime(df["datetime"])
        df = df.sort_values("datetime")
        st.dataframe(
            df[["patient_name", "datetime", "type", "status"]],
            column_config={
                "datetime": st.column_config.DatetimeColumn("Date & Time"),
                "status": st.column_config.SelectboxColumn(
                    "Status",
                    options=["scheduled", "completed", "cancelled"]
                )
            }
        )
    else:
        st.info("No appointments scheduled")
    
    # Recent activity
    st.subheader("Recent Activity")
    if appointments:
        recent = df.head(5)
        for _, row in recent.iterrows():
            st.write(f"📅 {row['datetime'].strftime('%Y-%m-%d %H:%M')} - {row['patient_name']} - {row['type']}")

elif page == "Patients":
    st.header("Patient Management")
    
    # Add new patient
    with st.expander("Add New Patient"):
        with st.form("new_patient"):
            name = st.text_input("Full Name")
            email = st.text_input("Email")
            phone = st.text_input("Phone Number")
            submitted = st.form_submit_button("Add Patient")
            if submitted:
                if create_patient(name, email, phone):
                    st.success("Patient added successfully!")
                else:
                    st.error("Failed to add patient. Please try again.")
    
    # Patient list
    st.subheader("Patient List")
    patients = get_patients()
    if patients:
        df = pd.DataFrame(patients)
        st.dataframe(
            df[["name", "email", "phone", "created_at"]],
            column_config={
                "created_at": st.column_config.DatetimeColumn("Created At")
            }
        )
    else:
        st.info("No patients registered")

elif page == "Appointments":
    st.header("Appointment Management")
    
    # Get patients for dropdown
    patients = get_patients()
    patient_options = {f"{p['name']} ({p['email']})": p['id'] for p in patients}
    
    # Schedule new appointment
    with st.expander("Schedule New Appointment"):
        with st.form("new_appointment"):
            patient_name = st.selectbox("Select Patient", options=list(patient_options.keys()))
            date = st.date_input("Date")
            time = st.time_input("Time")
            appointment_type = st.selectbox("Type", ["Check-up", "Follow-up", "Consultation"])
            notes = st.text_area("Notes")
            submitted = st.form_submit_button("Schedule")
            if submitted:
                patient_id = patient_options[patient_name]
                datetime_str = datetime.combine(date, time).isoformat()
                if create_appointment(patient_id, datetime_str, appointment_type, notes):
                    st.success("Appointment scheduled successfully!")
                else:
                    st.error("Failed to schedule appointment. Please try again.")
    
    # Appointment list
    st.subheader("Upcoming Appointments")
    appointments = get_appointments()
    if appointments:
        df = pd.DataFrame(appointments)
        df["datetime"] = pd.to_datetime(df["datetime"])
        df = df.sort_values("datetime")
        st.dataframe(
            df[["patient_name", "datetime", "type", "status", "notes"]],
            column_config={
                "datetime": st.column_config.DatetimeColumn("Date & Time"),
                "status": st.column_config.SelectboxColumn(
                    "Status",
                    options=["scheduled", "completed", "cancelled"]
                )
            }
        )
    else:
        st.info("No appointments scheduled")

elif page == "Settings":
    st.header("System Settings")
    
    # Notification settings
    st.subheader("Notification Settings")
    sms_enabled = st.checkbox("Enable SMS Notifications")
    email_enabled = st.checkbox("Enable Email Notifications")
    whatsapp_enabled = st.checkbox("Enable WhatsApp Notifications")
    
    # Reminder settings
    st.subheader("Reminder Settings")
    reminder_timing = st.slider(
        "Send reminders (hours before appointment)",
        min_value=1,
        max_value=48,
        value=24,
        step=1
    )
    
    # Save settings
    if st.button("Save Settings"):
        # TODO: Implement settings save
        st.success("Settings saved successfully!")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ for the hackathon") 