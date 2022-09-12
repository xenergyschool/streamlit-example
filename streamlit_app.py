from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import requests
import json

st.write("""
# Karir.ai Model Demo
Ini adalah AI Model demo untuk 'Job Description Generator' dari input 'Job Title' (english) text.
Klik 'Generate' beberapakali untuk menghasilkan deskripsi pekerjaan yang berbeda.
""")


def fetch(session, url, jobtitle):
    try:
        result = session.post(url, json={'jobtitle':jobtitle})
        return result.json()
    except Exception:
        return {}


def main():
    session = requests.Session()
    with st.form("my_form"):
        jobtitle = st.text_input("Masukan Job Title", "Javascript Developer")

        submitted = st.form_submit_button("Generate")

        if submitted:
            st.write("Result")
            data = fetch(session, f"https://t5-jobdesc-normalize-dnxwuwa5ra-et.a.run.app/getjobdesc" , jobtitle)
            if data:
                json_str = json.dumps(data)
                resp = json.loads(json_str)
                st.success(resp['jobdesc'])
            else:
                st.error("Error")


if __name__ == '__main__':
    main()