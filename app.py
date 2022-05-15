import numpy as np
import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

# Web App Title
st.markdown('''
# **DSPL Mini Project**

This is the **EDA App for University Rankings dataset**.

---
''')

# Upload CSV data
with st.sidebar.header('1. Upload your University CSV data'):
    uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
    


# Pandas Profiling Report

@st.cache
def load_csv():
    csv = pd.read_csv(uploaded_file)
    return csv
df = load_csv()
pr = ProfileReport(df, explorative=True)
st.header('**Input DataFrame**')
st.write(df)
st.write('---')
st.header('**Pandas Profiling Report**')
st_profile_report(pr)

