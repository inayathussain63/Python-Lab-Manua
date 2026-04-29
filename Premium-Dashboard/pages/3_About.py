import streamlit as st
from components.ui import load_css

st.set_page_config(page_title="About", page_icon="ℹ️", layout="centered")
load_css("styles/style.css")

st.markdown("<h1 style='text-align: center;'>ℹ️ About Project</h1>", unsafe_allow_html=True)
st.markdown("---")

st.markdown("""
### Premium Python Dashboard Toolkit
This project demonstrates the powerful capabilities of combining **Streamlit, Plotly, and Lottie** to create a highly polished, responsive, and industry-grade user interface for data products.

* **Tech Stack:** Python 3.9+, Streamlit, Plotly Express
* **UI Features:** Glassmorphism, CSS Variables, Background Gradients, CSS Keyframe Animations
* **Use Cases:** Machine Learning Portfolios, Admin Panels, Executive Dashboards.

---

**Developed for AI interface excellence.**
""")
