import streamlit as st
from components.ui import load_css

st.set_page_config(page_title="Settings", page_icon="⚙️", layout="centered")
load_css("styles/style.css")

st.markdown("<h1 style='text-align: center;'>⚙️ User Settings</h1>", unsafe_allow_html=True)
st.markdown("---")

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("### Profile Preferences")
    username = st.text_input("Username", "admin")
    email = st.text_input("Email", "admin@domain.com")
    st.button("Update Profile")

with col2:
    st.markdown("### Display Options")
    theme = st.selectbox("Application Theme", ["Dark / Futuristic", "System Default"])
    animations = st.checkbox("Enable Lottie Animations", True)
    graphs = st.checkbox("Enable Interactive Graphs", True)
    st.button("Save Preferences")
