import pandas as pd
import streamlit as st


@st.cache_data
def get_pyladies_locations_data():
    types={
    'city': 'string',
    'country': 'string',
    'longitude': 'float64',
    'latitude': 'float64'
    }
    df = pd.read_csv("app/data/pyladies_locations.csv", dtype=types)
    return df


@st.cache_data
def get_pyconlt_data():
    # TODO - can we get the latest?
    df = pd.read_csv("app/data/2025-03-15-202017--pyconlt-talks.csv")
    return df