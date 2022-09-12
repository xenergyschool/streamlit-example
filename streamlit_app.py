from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import requests

st.write("""
# Karir.ai Model Demo
Ini adalah AI Model demo untuk 'Job Description Generator' dari input 'Job Title' 
""")


def fetch(session, url, params):
    try:
        result = session.post(url, json=params)
        return result.json()
    except Exception:
        return {}


def main():
    st.set_page_config(page_title="KarirAi Demo App", page_icon="🤖")
    st.title("KarirAi Demo Only")
    session = requests.Session()
    with st.form("my_form"):
        jobtitle = st.text_input("Masukan Job Title", "Javascript Developer")

        submitted = st.form_submit_button("Submit")

        if submitted:
            st.write("Result")
            data = fetch(session, f"https://t5-jobdesc-normalize-dnxwuwa5ra-et.a.run.app/getjobdesc" , "{'jobtitle':'{jobtitle}'}")
            if data:
                st.success(data['jobdesc'])
            else:
                st.error("Error")


if __name__ == '__main__':
    main()