import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
from streamlit_lottie import st_lottie
from components.ui import load_css, glassmorphism_card, load_lottieurl

st.set_page_config(
    page_title="Premium Dashboard | Home",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load custom CSS
load_css("styles/style.css")

# --- UI Layout --- #

st.sidebar.markdown("## ✨ Navigation")
st.sidebar.markdown("Welcome to the Premium Dashboard")
st.sidebar.markdown("---")

# Main Content
st.markdown("<h1 style='text-align: center;'>✨ Premium SaaS Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #94a3b8; font-size: 1.2rem;'>Welcome to the future of interactive data visualization analytics.</p>", unsafe_allow_html=True)
st.markdown("---")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### Overview Analytics")
    c1, c2, c3 = st.columns(3)
    with c1:
        glassmorphism_card("Total Users", "12,450", "▲ +15% this week", desc_color="#10b981")
    with c2:
        glassmorphism_card("Revenue", "$45.2K", "▲ +8% this week", desc_color="#10b981")
    with c3:
        glassmorphism_card("Active Sessions", "3,210", "▼ -2% this week", desc_color="#ef4444")
        
    st.markdown("### User Engagement Trends")
    # Sample Plotly Chart
    np.random.seed(42)
    df = pd.DataFrame({
        "Date": pd.date_range(start="2026-04-01", periods=30, freq="D"),
        "Sessions": np.random.randn(30).cumsum() + 100
    })
    
    fig = px.area(df, x="Date", y="Sessions", template="plotly_dark", 
                 color_discrete_sequence=["#8b5cf6"],
                 height=350)
    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font_color="#f8fafc",
        margin=dict(l=20, r=20, t=30, b=20)
    )
    st.plotly_chart(fig, width="stretch")

with col2:
    lottie_dashboard = load_lottieurl("https://lottie.host/819d9baf-f69c-44b4-a4b8-2ce8cf60b643/kX0FzL47dZ.json")
    if lottie_dashboard:
        st_lottie(lottie_dashboard, height=300, key="dashboard_animation")
    
    st.markdown("### Recent Activity")
    st.info("🔔 Server deployed successfully.")
    st.success("🔔 Machine learning model v2.1 trained.")
    st.warning("🔔 Anomaly detected in traffic.")

st.markdown("---")
st.markdown("<p style='text-align: center; color: #64748b;'>built with Python, Streamlit, and Plotly</p>", unsafe_allow_html=True)