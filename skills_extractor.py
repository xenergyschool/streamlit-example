from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import requests
import json

st.write("""
# Karir.ai Model Demo
Ini adalah AI Model demo untuk 'Skills Extractor' dari input 'Job Description' (english / bahasa indonesia) text.
""")


def fetch(session, url, jobdesc):
    try:
        result = session.post(url, json={'text':jobdesc})
        return result.json()
    except Exception:
        return {}


def main():
    session = requests.Session()
    with st.form("my_form"):
        jobdesc = st.text_input("Masukan Job Description", "Arvis is a SaaS Workflow Automation solution platform in Indonesia. We are at the early stage of a startup. If your passion is to build something new, explore new things. Come and join us. What You Will be Doing ● Design and prototype new services and applications, also build back-end frameworks that are maintainable, flexible, and scalable. ● Compile and analyze data, processes, and codes to troubleshoot problems, and able to identify areas for improvement. ● Collaborate with Front-End Developers (web & mobile)  and Head of Tech to create goals and functional design, also cohesive codes to improve user experience. ● Collaborate with Front-End Developers and Head of Tech to create goals and functional design, also cohesive codes to improve user experience. ● Manage Deployment to development, staging, and production environment. Who Is Our Ideal Candidate ● 1 - 3 years of work experience as a Back-End Developer ● Good experience with Web API, MongoDB, SQL, Redis, and Node.js ● Expertise in best practices, design patterns, architecture, data modeling and authentication protocols ● Good understanding of software engineering concepts, and algorithms. ● Curiosity to explore creative solutions and try new things ● Familiar with AWS technology ● Having experience in a B2B industry will be a plus")

        submitted = st.form_submit_button("Dapatkan Daftar Skills")

        if submitted:
            st.write("Result")
            data = fetch(session, f"https://us-central1-socialmediaprofiler.cloudfunctions.net/skillExtract" , jobdesc)
            if data:
                st.success(data)
            else:
                st.error("Error")


if __name__ == '__main__':
    main()