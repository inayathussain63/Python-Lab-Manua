import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
from components.ui import load_css

st.set_page_config(page_title="Analytics", page_icon="📊", layout="wide")
load_css("styles/style.css")

st.markdown("<h1>📊 Deep Analytics</h1>", unsafe_allow_html=True)
st.markdown("---")

df_heat = pd.DataFrame(np.random.randint(0, 100, size=(10, 10)), columns=list('ABCDEFGHIJ'))

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("### User Retention Map")
    fig = px.imshow(df_heat, color_continuous_scale="Viridis", template="plotly_dark")
    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig, width="stretch")

with col2:
    st.markdown("### Traffic Distribution")
    df_pie = pd.DataFrame({
        "Channels": ["Direct", "Organic", "Paid", "Referral", "Social"],
        "Values": [40, 25, 15, 10, 10]
    })
    fig2 = px.pie(df_pie, names="Channels", values="Values", hole=0.5, template="plotly_dark",
                  color_discrete_sequence=px.colors.sequential.Plasma)
    fig2.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig2, width="stretch")
