import streamlit as st
import scouting_st
import prediction_st

st.set_page_config(
        page_title="Football Talent Scout",
        # page_icon="",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            'About': "My Github Profile https://github.com/BintangRamadhan837"
        }
    )

pages = {
    "Talent Scouting": scouting_st,
    "Prediction Wage": prediction_st
}

st.sidebar.title("Football Talent Scout")
selection = st.sidebar.selectbox("Pages", list(pages.keys()))
page =pages[selection]
page.app1()