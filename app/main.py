import streamlit as st
from dashboard import pyladies


def main():
    pg = st.navigation(
        [
            st.Page(pyladies.show_pyladies_locations_page, title="PyLadies locations"),
        ]
    )
    pg.run()


if __name__ == "__main__":
    main()
