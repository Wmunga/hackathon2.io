import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta
import requests

# Page config
st.set_page_config(
    page_title="HealthTech Reminder System",
    page_icon="🏥",
    layout="wide"
)

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
    
    # Quick stats
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Today's Appointments", "5")
    with col2:
        st.metric("Pending Reminders", "12")
    with col3:
        st.metric("Completed Today", "3")
    with col4:
        st.metric("No-Shows", "1")
    
    # Calendar view
    st.subheader("Upcoming Appointments")
    # TODO: Implement calendar view
    
    # Recent activity
    st.subheader("Recent Activity")
    # TODO: Implement activity feed

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
                # TODO: Implement patient creation
                st.success("Patient added successfully!")
    
    # Patient list
    st.subheader("Patient List")
    # TODO: Implement patient list

elif page == "Appointments":
    st.header("Appointment Management")
    
    # Schedule new appointment
    with st.expander("Schedule New Appointment"):
        with st.form("new_appointment"):
            patient = st.selectbox("Select Patient", ["Patient 1", "Patient 2"])  # TODO: Get from API
            date = st.date_input("Date")
            time = st.time_input("Time")
            appointment_type = st.selectbox("Type", ["Check-up", "Follow-up", "Consultation"])
            notes = st.text_area("Notes")
            submitted = st.form_submit_button("Schedule")
            if submitted:
                # TODO: Implement appointment creation
                st.success("Appointment scheduled successfully!")
    
    # Appointment list
    st.subheader("Upcoming Appointments")
    # TODO: Implement appointment list

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