# komunikasi backend(flask) dengan frontend(streamlit)
import pandas
import streamlit as st
import requests
from PIL import Image


def app1():
    image = Image.open('messipep.jpg')
    st.image(image, caption='Lamasia Academy', width=850)

    st.markdown("<h1 style='text-align: center; color: black;'>Aplikasi Prediksi Gaji Pemain</h1>", unsafe_allow_html=True)

    with st.container():
    # with st.expander('MAIN INFO'):
        st.markdown("<h5 style='text-align: center; color: black;'>MAIN INFO</h5>", unsafe_allow_html=True)
        st.text_input('Name')
        st.text_input('Nationality')
        st.selectbox('Position', ['Goalkeeper', 'Center Back', 'Left Wing Back', 'Right Wing Back', 'Defensive Midfielder', 'Center Midfielder', 'Attack Midfielder', 'Right Wing', 'Left Wing', 'Striker'])
        col1_1, col1_2, col1_3 = st.columns(3)
        with col1_1:
            overall = st.number_input('overall')
            potential = st.number_input('potential')
            value = st.number_input('value')
        with col1_2:
            age = st.number_input('age')
            height = st.number_input('height')
            weight = st.number_input('weight')
        with col1_3:
            international_reputation = st.number_input('international_reputation')
            weak_foot = st.number_input('weak_foot')
            preferred_foot = st.selectbox('preferred_foot', ['Right', 'Left'])

    with st.container():
    # with st.expander('ATTACKING'):
        st.markdown("<h5 style='text-align: center; color: black;'>ATTACKING</h5>", unsafe_allow_html=True)
        col2_1, col2_2, col2_3 = st.columns(3)
        with col2_1:           
            finishing = st.number_input('finishing')
            headingaccuracy = st.number_input('headingaccuracy')
        with col2_2:
            crossing = st.number_input('crossing')
            volleys = st.number_input('volleys')
        with col2_3:
            shortpassing = st.number_input('shortpassing')
            skill_moves = st.number_input('skill_moves')

    with st.container():
    # with st.expander('SKILL'):
        st.markdown("<h5 style='text-align: center; color: black;'>SKILL</h5>", unsafe_allow_html=True)
        col3_1, col3_2, col3_3 = st.columns(3)
        with col3_1:
            dribbling = st.number_input('dribbling')
            curve = st.number_input('curve')
        with col3_2:
            fkaccuracy = st.number_input('fkaccuracy')
            longpassing = st.number_input('longpassing')
        with col3_3:
            ballcontrol = st.number_input('ballcontrol')

    with st.container():
    # with st.expander('MOVEMENT'):
        st.markdown("<h5 style='text-align: center; color: black;'>MOVEMENT</h5>", unsafe_allow_html=True)
        col4_1, col4_2, col4_3 = st.columns(3)
        with col4_1:
            acceleration = st.number_input('acceleration')
            sprintspeed = st.number_input('sprintspeed')
        with col4_2:
            agility = st.number_input('agility')
            reactions = st.number_input('reactions')
        with col4_3:
            balance = st.number_input('balance')

    with st.container():
    # with st.expander('POWER'):
        st.markdown("<h5 style='text-align: center; color: black;'>POWER</h5>", unsafe_allow_html=True)
        col5_1, col5_2, col5_3 = st.columns(3)
        with col5_1:
            shotpower = st.number_input('shotpower')
            jumping = st.number_input('jumping')
        with col5_2:
            stamina = st.number_input('stamina')
            strength = st.number_input('strength')
        with col5_3:
            longshots = st.number_input('longshots')

    with st.container():
    # with st.expander('MENTALITY'):
        st.markdown("<h5 style='text-align: center; color: black;'>MENTALITY</h5>", unsafe_allow_html=True)
        col6_1, col6_2, col6_3 = st.columns(3)
        with col6_1:
            aggression = st.number_input('aggression')
            interceptions = st.number_input('interceptions')
        with col6_2:
            positioning = st.number_input('positioning')
            vision = st.number_input('vision')
        with col6_3:
            penalties = st.number_input('penalties')
            composure = st.number_input('composure')

    with st.container():
        st.markdown("<h5 style='text-align: center; color: black;'>DEFENDING</h5>", unsafe_allow_html=True)
        col7_1, col7_2, col7_3 = st.columns(3)
        with col7_1:
            marking = st.number_input('marking')
        with col7_2:
            standingtackle = st.number_input('standingtackle')
        with col7_3:
            slidingtackle = st.number_input('slidingtackle')

    data = {'preferred_foot':preferred_foot,
            'age':age,
            'overall':overall,
            'potential':potential,
            'value':value,
            'international_reputation':international_reputation,
            'weak_foot':weak_foot,
            'skill_moves':skill_moves,
            'height':height,
            'weight':weight,
            'crossing':crossing,
            'finishing':finishing,
            'headingaccuracy':headingaccuracy,
            'shortpassing':shortpassing,
            'volleys':volleys,
            'dribbling':dribbling,
            'curve':curve,
            'fkaccuracy':fkaccuracy,
            'longpassing':longpassing,
            'ballcontrol':ballcontrol,
            'acceleration':acceleration,
            'sprintspeed':sprintspeed,
            'agility':agility,
            'reactions':reactions,
            'balance':balance,
            'shotpower':shotpower,
            'jumping':jumping,
            'stamina':stamina,
            'strength':strength,
            'longshots':longshots,
            'aggression':aggression,
            'interceptions':interceptions,
            'positioning':positioning,
            'vision':vision,
            'penalties':penalties,
            'composure':composure,
            'marking':marking,
            'standingtackle':standingtackle,
            'slidingtackle':slidingtackle}

    URL = "https://bintang-fifa-backend.herokuapp.com/predict"

    #komunikasi
    r = requests.post(URL, json=data)
    res = r.json()

    if st.button('Prediksi Gaji'):
        st.title(res['data']['result'])

    # with st.container():
    #     col1,col2,col3 = st.columns(3)
    #     with col1:
    #         st.write('')
    #     with col2:
    #         if res['code'] == 200:
    #             if st.button('Prediksi Gaji'):
    #                 st.title(res['data']['result'])
    #         else:
    #             st.write('Mohon maaf terjadi kesalahan')
    #             st.write(f"keterangan : {res['summary']}")
    #     with col3:
    #         st.write('')

