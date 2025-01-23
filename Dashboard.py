import streamlit as st 
import pandas as pd
import seaborn as sns
import os

df = pd.read_csv('https://raw.githubusercontent.com/Quera-fr/Python-Programming/refs/heads/main/data.csv')

# Title
st.title('My Dashboard')

# Subtitle
st.subheader('Présentation de données')

# Champ de texte
name = st.text_input('Entrez votre nom')

if(name):
    st.write(f'Bonjour, {name}')

if st.checkbox('Voulez-vous gagner 10 bitcoins par secondes ???'):
    # Video
    st.video('https://www.youtube.com/watch?v=dQw4w9WgXcQ', autoplay=True)
# Text
st.write('Présentation de données avec Streamlit')

try : 
    st.sidebar.write(st.secrets['API_KEY'])
except :
    st.sidebar.error('API_KEY not found')

st.set_page_config(
    page_title='My Dashboard',
    page_icon='👀',
    layout='centered', 
    initial_sidebar_state='auto'
)

# Checkbox
if(st.checkbox('Afficher le formulaire')):
    with st.form(key='my_form'):

        col1, col2 = st.columns(2)
        
        with col1:
            # Selectbox 
            profession = st.selectbox('Choisissez une profession', df['Profession'].unique())
                
            # Slider
            age = st.slider('Sélectionnez une tranche âge', df.Age.min(), df.Age.max(), value=[df.Age.min(), df.Age.max()])

        with col2:
            if(st.form_submit_button('Valider')) :
                if(profession) :
                    if(age):
                        data_age = df[(df['Profession'] == profession) & (df.Age>age[0]) & (df.Age<age[1])].Age
                        plot = sns.histplot(data_age, bins=age[1]-age[0])
                        if(plot) :
                            st.pyplot(plot.figure)
                            st.success('Les données ont été affichées avec succès')
                        else :
                            st.error('Les données n\'ont pas pu être affichées')

    # Dataframe
    st.write(df)