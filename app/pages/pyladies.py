import streamlit as st
from utils import get_pyladies_locations_data


def show_pyladies_locations_page():
    st.title("PyLadies around the world!")
    st.write("This page shows the locations of PyLadies groups around the world based on the PyLadies website.")

    df = get_pyladies_locations_data()

    st.dataframe(df)
