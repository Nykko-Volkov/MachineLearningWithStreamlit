import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt





df = pd.read_csv(r"C:\Users\Lenovo\OneDrive\Desktop\MachineLearningWithStreamlit\StreamlitBasedDashboard\quarterly_canada_population.csv")
st.title("Canada Quarterly Population Dashboard")
st.subheader("An interactive dashboard to visualize quarterly population data of Canada.")
st.dataframe(df)


with st.form("population-form"):
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("Choose a starting date")
        start_quarter = st.selectbox("Quarter", options=["Q1", "Q2", "Q3", "Q4"], index=2, key="start_q")
        start_year = st.slider("Year", min_value=1991, max_value=2023, value=1991, step=1, key="start_y")

    with col2:
        st.write("Choose an end date")
        end_quarter = st.selectbox("Quarter", options=["Q1", "Q2", "Q3", "Q4"], index=0, key="end_q")
        end_year = st.slider("Year", min_value=1991, max_value=2023, value=2023, step=1, key="end_y")
        
    with col3:
        st.write("Choose a location")
        target = st.selectbox("Choose a location", options=df.columns[1:], index=0)

    submit_btn = st.form_submit_button("Analyze", type="primary")



st.bar_chart(df, x="Quarter", y=target)
st.line_chart(df, x="Quarter", y=target)