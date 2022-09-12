from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

st.write("""
# Karir.ai Model Demo
Ini adalah AI Model demo untuk 'Job Description Generator' dari input 'Job Title' 
""")

jobtitle = st.text_input("Masukan Job Title", " Javascript Developer")
jobdesc = st.button("Generate JobDesc")

if jobdesc:
    st.success(f"Job descripton here...!")