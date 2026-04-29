import streamlit as st
import requests

def load_lottieurl(url: str):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except Exception as e:
        return None

def glassmorphism_card(title, value, description="", desc_color="#10b981"):
    st.markdown(f"""
    <div class="glass-card">
        <div class="glass-card-title">{title}</div>
        <div class="glass-card-value neon-text">{value}</div>
        <div class="glass-card-desc" style="color: {desc_color};">{description}</div>
    </div>
    """, unsafe_allow_html=True)
    
def load_css(file_name="styles/style.css"):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
