import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Configuration
st.set_page_config(page_title="Maharashtra IDD", layout="wide")

# 2. Data Loading (Consolidating d3, d4, d6)
@st.cache_data
def load_data():
    return pd.read_csv("data/maharashtra_gddp.csv")

df = load_data()

# 3. Sidebar for District Selection & Alerts
with st.sidebar:
    st.title("District Control Panel")
    selected_dist = st.selectbox("Select District", df['District'].unique())
    
    # Live Alert Logic
    target_val = df[df['District'] == selected_dist]['2027-28'].iloc[0]
    if target_val < 50000: # Example Threshold
        st.error(f"🚨 Alert: {selected_dist} below growth trajectory!")

# 4. Economic War Room (Visualizing d6.jpg)
st.header(f"Economic War Room: {selected_dist}")
col1, col2 = st.columns(2)
col1.metric("2027-28 Target (₹ Cr)", f"{target_val:,}")
col2.metric("State Contribution (%)", "12.5%") # Example logic

# 5. Sectoral Deep-Dive (Visualizing d4, d5)
fig = px.bar(df, x='Sector', y='Value', title="Sectoral Composition")
st.plotly_chart(fig, use_container_width=True)