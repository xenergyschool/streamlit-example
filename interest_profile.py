from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import requests
import json

st.write("""
# Karir.ai Model Demo
Ini adalah AI Model demo untuk 'Interest (RIASEC) profile' dari input Job Title & Job Description text.
Untuk hasil yang optimal, input hanya terdiri dari 1 kalimat deskripsi / detail pekerjaan.
""")


def fetch(session, url, jobtitle, jobdesc):
    try:
        result = session.post(url, json={'jobtitle':jobtitle , 'jobdesc':jobdesc})
        return result.json()
    except Exception:
        return {}


def main():
    session = requests.Session()
    with st.form("my_form"):
        jobtitle = st.text_input("Masukan Job Title", "Javascript Developer")
        jobdescription = st.text_input("Masukan Job Description", "Evaluating code to ensure it is valid, properly structured, meets standards and is compatible with browsers, devices or operating systems.")


        submitted = st.form_submit_button("Dapatkan Profile Interest")

        if submitted:
            st.write("Result :")
            data = fetch(session, f"https://interestprofile-dnxwuwa5ra-et.a.run.app/getinterestprofile" , jobtitle, jobdescription)
            if data:
                json_str = json.dumps(data)
                resp = json.loads(json_str)
                st.success(resp['interestprofile'])
            else:
                st.error("Error")


if __name__ == '__main__':
    main()