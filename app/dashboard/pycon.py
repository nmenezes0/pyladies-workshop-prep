import streamlit as st

from utils import get_pyconlt_data


def show_pycon_data_page():
    st.title("PyCon LT talks")
    st.write("This page shows the talks from PyCon LT based on the PyCon LT website.")

    df = get_pyconlt_data()
    st.dataframe(df)