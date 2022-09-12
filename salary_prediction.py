from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import requests
import json

st.write("""
# Karir.ai Model Demo
Ini adalah AI Model demo untuk 'Salary Prediction' dari input Job Title, Job Description dan Lokasi (english & indonesian) text.
Hasil prediksi bersifat rata-rata di berbagai macam industri. Beberapa perusahaan & industri mungkin memiliki nilai yang lebih tinggi.
""")


def fetch(session, url, jobtitle, jobdesc, location):
    try:
        result = session.post(url, json={'jobtitle':jobtitle , 'jobdesc':jobdesc , 'location': location})
        return result.json()
    except Exception:
        return {}


def main():
    session = requests.Session()
    with st.form("my_form"):
        jobtitle = st.text_input("Masukan Job Title", "Javascript Developer")
        jobdescription = st.text_input("Masukan Job Description", "Evaluating code to ensure it is valid, properly structured, meets standards and is compatible with browsers, devices or operating systems.")
        location = st.text_input("Masukan lokasi pekerjaan", "Jakarta")

        submitted = st.form_submit_button("Dapatkan Prediksi Salary")

        if submitted:
            st.write("Result :")
            data = fetch(session, f"https://salary-predictor-dnxwuwa5ra-et.a.run.app/getsalarypredictor" , jobtitle, jobdescription, location)
            if data:
                json_str = json.dumps(data)
                resp = json.loads(json_str)
                st.success(resp['salaryprediction'])
            else:
                st.error("Error")


if __name__ == '__main__':
    main()