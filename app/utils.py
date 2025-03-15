import os

import pandas as pd
import streamlit as st


@st.cache_data
def get_pyladies_locations_data():
    st.write(os.getcwd())
    return pd.read_csv("app/data/pyladies_locations.csv")
