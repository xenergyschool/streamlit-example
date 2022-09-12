from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import requests
import json

st.write("""
# Karir.ai Model Demo
Ini adalah AI Model demo untuk 'Related Skills' dari input 'skills' (dictionary / list of skills).
Contoh beberapa skills : JavaScript Frameworks, Business Development, Market Penetration, Model View Controller
""")


def fetch(session, url, skill):
    try:
        result = session.post(url, json={'skills':skill})
        return result.json()
    except Exception:
        return {}


def main():
    session = requests.Session()
    with st.form("my_form"):
        skill = st.text_input("Masukan Skills", "CSS Frameworks")

        submitted = st.form_submit_button("Lihat Related Skills")

        if submitted:
            st.write("Result")
            data = fetch(session, f"https://us-central1-socialmediaprofiler.cloudfunctions.net/relatedSkills" , skill)
            if data:
                st.success(data)
            else:
                st.error("Error")


if __name__ == '__main__':
    main()