import streamlit as st
from dashboard import pyladies, pycon


def main():
    pg = st.navigation(
        [
            st.Page(pyladies.show_pyladies_locations_page, title="PyLadies locations"),
            st.Page(pycon.show_pycon_data_page, title="PyCon LT talks"),
        ]
    )
    pg.run()


if __name__ == "__main__":
    main()
