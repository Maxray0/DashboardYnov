import streamlit as st 
import pandas as pd
import seaborn as sns

st.set_page_config(
    page_title='My Dashboard',
    page_icon='🖖',
    layout='centered', 
    initial_sidebar_state='auto'
)

df = pd.read_csv('https://raw.githubusercontent.com/Quera-fr/Python-Programming/refs/heads/main/data.csv')

# Title
st.title('My Dashboard')

# Subtitle
st.subheader('Présentation de données')

# Champ de texte
name = st.text_input('Entrez votre nom')

if(name):
    st.write(f'Bonjour, {name}')

# Text
st.write('Présentation de données avec Streamlit')




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

# Image
st.sidebar.image('https://media.istockphoto.com/id/1448152453/vector/big-data-technology-and-data-science-illustration-data-flow-concept-querying-analysing.jpg?s=612x612&w=0&k=20&c=To0lhCrVmDYdSkOUOGxGsjlYe0buj_wwGCDqYhF9p2o=')

# Video
st.sidebar.video('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
