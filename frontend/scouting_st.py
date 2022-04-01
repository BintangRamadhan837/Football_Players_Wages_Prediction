import streamlit as st
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

def app1():
    df = pd.read_csv('data.csv')

    image = Image.open('scouting.png')
    st.image(image, caption='Football Talent Scout', width=850)

    st.title('Scouting')

    with st.container():
    # with st.expander('age'):
        col1, col2, col3 = st.columns(3)
        with col1:
            Age1 = df.sort_values("Age")['Age'].unique()
            Potential = df.groupby("Age")["Potential"].mean().values
            fig1 = plt.figure(figsize=(10, 6))
            plt.title('Mean Potential vs Age')
            plt.xlabel('Age', fontsize=15)
            plt.ylabel('player Potential', fontsize=15)
            sns.set_style("whitegrid")
            sns.lineplot(x=Age1, y=Potential)
            plt.legend(loc=4, prop={'size': 15}, frameon=True,shadow=True, facecolor="white", edgecolor="black")
            st.pyplot(fig1)
        with col2:
            Age2 = df.sort_values("Age")['Age'].unique()
            Overall = df.groupby("Age")["Overall"].mean().values
            fig2 = plt.figure(figsize=(10, 6))
            plt.title('Mean Overall vs Age')
            plt.xlabel('Age', fontsize=15)
            plt.ylabel('player Overall', fontsize=15)
            sns.set_style("whitegrid")
            sns.lineplot(x=Age2, y=Overall, label="Overall")
            plt.legend(loc=4, prop={'size': 15}, frameon=True,shadow=True, facecolor="white", edgecolor="black")
            st.pyplot(fig2)
        with col3:
            Age3 = df.sort_values("Age")['Age'].unique()
            Stamina = df.groupby("Age")["Stamina"].mean().values
            fig3 = plt.figure(figsize=(10, 6))
            plt.title('Mean Stamina vs Age')
            plt.xlabel('Age', fontsize=15)
            plt.ylabel('player Stamina', fontsize=15)
            sns.set_style("whitegrid")
            sns.lineplot(x=Age3, y=Stamina)
            plt.legend(loc=4, prop={'size': 15}, frameon=True,shadow=True, facecolor="white", edgecolor="black")
            st.pyplot(fig3)


    with st.container():

        # st.header("Preferred Foot")
        fig = plt.figure(figsize=(5,4))
        st.write(sns.countplot(x="Preferred Foot", hue = "Preferred Foot", data =df, palette='viridis').set_title("Preferred Foot"))
        st.pyplot(fig)

    # with st.container():
    #     with st.expander('potential'):
    #         # Maean player potential score per country
    #         country_potential = df.groupby("Nationality")["Potential"].mean()
    #         country_potential = country_potential.reset_index()

    #         data = [ dict(
    #                 type = 'choropleth',
    #                 locationmode = "country names",
    #                 locations = country_potential['Nationality'],
    #                 z = country_potential['Potential'],
    #                 colorscale = [[65,"rgb(5, 10, 172)"],[67,"rgb(40, 60, 190)"],[69,"rgb(70, 100, 245)"],\
    #                     [71,"rgb(90, 120, 245)"],[73,"rgb(106, 137, 247)"],[75,"rgb(220, 220, 220)"]],
    #                 autocolorscale = False,
    #                 reversescale = True,
    #                 marker = dict(
    #                     line = dict (
    #                         color = 'rgb(180,180,180)',
    #                         width = 0.5
    #                     ) ),
    #                 colorbar = dict(
    #                     autotick = False,
    #                     title = 'Mean<br>Potential Score'),
    #             ) ]

    #         layout = dict(
    #             title = 'Mean Player Potential',
    #             geo = dict(
    #                 showframe = False,
    #                 showcoastlines = False,
    #                 projection = dict(
    #                     type = 'Mercator'
    #                 )
    #             )
    #         )

    #         fig = dict( data=data, layout=layout )
    #         py.iplot( fig, validate=False )