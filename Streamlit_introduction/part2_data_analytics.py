import streamlit as st
import pandas as pd


data = pd.read_csv(r'C:\Users\Lenovo\OneDrive\Desktop\MachineLearningWithStreamlit\Streamlit_introduction\sample.csv')
st.dataframe(data)

st.line_chart(data,x='year',y=["col1","col2","col3"])
st.bar_chart(data,x='year',y=["col1","col2","col3"])
st.area_chart(data,x='year',y=["col1","col2","col3"])

