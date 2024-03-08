import pandas as pd
import streamlit as st
st.sidebar.header("Choose a module!", divider='rainbow')
import re

import plotly.express as px
import plotly.io as pio

import seaborn as sns
import matplotlib.pyplot as plt

def columnPicker(df):
        st.header('Grouping by a Nominal Attribute')
        x = st.selectbox('**Select the nominal attribute, X**', df.columns)
        y = st.selectbox('**Select first measure, Y**', df.columns)
        z = st.selectbox('**Select extra measure, Z**', df.columns)     
        return x, y, z

# Design the visualisation
def charts():
        
            tab1, tab2, tab3 = st.tabs(['Bar chart', 'Scatter plot', 'Line chart'])
            with tab1:
                fig = px.bar((df), x=x, y=y, color=z, title=f'{x} vs {y} by {z}')
                st.plotly_chart(fig)
            
            with tab2:
                fig = px.scatter((df), x=x, y=y, color=z, title=f'{x} vs {y} by {z}')
                st.plotly_chart(fig)
            
            with tab3:
                fig = px.line((df), x=x, y=y, color=z, title=f'{x} vs {y} by {z}')
                st.plotly_chart(fig)
                  

def createTable(df):
    df = df.copy() # Copy of the frame to break the reference to the original frame

    st.write('This is the dataset')
    st.write(df, use_container_width=True)        

    st.markdown(
        """
        <style>
            div[data-testid="stFullScreenFrame"] {
                text-align: center;
            }
        </style>
    """, unsafe_allow_html=True)


df = st.session_state.df

createTable(df)

x, y, z = columnPicker(df)

if st.button(":green[Explore]"):
    st.subheader("Explore the Data in Diagrams")
    st.write('Click on tabs to explore')
    container = st.container()
    charts()