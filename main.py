# Design Home Page
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import streamlit as st
from streamlit_option_menu import option_menu

import pandas as pd
import numpy as np
from recommendation import get_description_recommendations, get_recommendations, get_title_recommendations

st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'mailto:mk797@cphbusiness.dk',
        'About': "https://docs.streamlit.io"
    }
)

banner = """
    <body style="background-color:yellow;">
            <div style="background-image: linear-gradient(90deg, rgb(255, 75, 75), rgb(28, 3, 204)); ;padding:10px">
                <h2 style="color:white;text-align:center;">Movie recommender</h2>
                <h3 style="color:white;text-align:center;"> By Magnus, Peter and Yusuf </h3>
            </div>
    </body>
    <br>
    """

try:
    df = pd.read_csv('./data/tmdb_5000_movies.csv')
except:
    st.error("No data found")

st.markdown(banner, unsafe_allow_html=True)

with st.expander("Select a title"):
    with st.form('titleForm'):
        titleSelect = st.selectbox("Select a title:", df['title'].values, index=None, placeholder='Choose a title')                
        submit = st.form_submit_button('Submit')
        if submit:
            if titleSelect != None:
                
                col1, col2 = st.columns([1, 13])
                with col1:
                    st.write("Selected movie: ")
                with col2:
                    st.write(df[df['title'] == titleSelect])

                result = get_title_recommendations(df, titleSelect)
                st.write(result)
            else:
                st.write("No title selected")

with st.expander("Select a description"):
    with st.form('descriptionForm'):
        descriptionSelect = st.selectbox("Select a description:", df['overview'].values, index=None, placeholder='Choose a description')                
        submit = st.form_submit_button('Submit')
        if submit:
            if descriptionSelect != None:
                col1, col2 = st.columns([1, 13])
                with col1:
                    st.write("Selected movie: ")
                with col2:
                    st.write(df[df['overview'] == descriptionSelect])

                result = get_description_recommendations(df, descriptionSelect)
                st.write(result)
            else:
                st.write("No description selected")

with st.expander("Choose a column"):
    columnSelect = st.selectbox("Select a column:", df.columns, index=None, placeholder='Choose a column')   

    if columnSelect != None:
        inputSelect = st.text_input("Enter input:", value='', max_chars=None, key=None, type='default', help=None, placeholder='Enter input')
        submit2 = st.button('Submit', key="submit2")
        if submit2:
            if inputSelect != None:
                result = get_recommendations(df, inputSelect, columnSelect)
                st.write(result)
            else:
                st.write("No input selected")