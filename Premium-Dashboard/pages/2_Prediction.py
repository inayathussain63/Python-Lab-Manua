import streamlit as st
import time
from components.ui import load_css

st.set_page_config(page_title="Predictions", page_icon="🤖", layout="centered")
load_css("styles/style.css")

st.title("🤖 Prediction Engine")
st.markdown("---")

st.markdown("### Run AI Prediction Model")

col1, col2 = st.columns([1, 2])

with col1:
    feature_1 = st.slider("Select feature value 1", 0, 100, 50)
    feature_2 = st.slider("Select feature value 2", 0.0, 1.0, 0.5)
    run_model = st.button("Generate Prediction ✨")

with col2:
    if run_model:
        st.info("Initializing neural network...")
        progress_bar = st.progress(0)
        
        for percent_complete in range(100):
            time.sleep(0.01)
            progress_bar.progress(percent_complete + 1)
            
        st.success("Analysis Complete!")
        
        confidence = (feature_1 * 0.8) + (feature_2 * 20)
        st.markdown(f"**Confidence Score:** {confidence:.2f}%")
        st.balloons()
    else:
        st.markdown("Awaiting input data...")
