import streamlit as st 
import pandas as pd
import seaborn as sns


st.set_page_config(
    page_title="My Dashboard",
    page_icon="👀",
    layout="wide",
)

@st.cache_data
def load_data():
    return pd.read_csv("https://raw.githubusercontent.com/Quera-fr/Python-Programming/refs/heads/main/data.csv")

try:
    st.sidebar.write(st.secrets['API_KEY'])
except:
    st.error('il n\'y a pas de clé API')

df = load_data()

st.title('My Dashboard')

if st.checkbox('Voulez-vous gagner 10 bitcoins par secondes ???'):
    # Video
    st.video('https://www.youtube.com/watch?v=dQw4w9WgXcQ', autoplay=True)

st.subheader('Presentation de data')

st.write('Presentation des data avec streamlit')

if st.checkbox('Afficher le df'):

    st.write(df)

if st.checkbox('Afficher le formulaire'):

    name = st.text_input('Entrez votre nom')
    if name != "":
        st.write(f"Salut, {name}")

with st.form(key='my_form'):
    
    col1, col2 = st.columns(2)
    
    with col1:
        profession = st.selectbox("Selectioné une profession", df.Profession.unique())
        
        age = st.slider("Selectionnez un age", df.Age.min(), df.Age.max(), (df.Age.min(), df.Age.max()))
        valid = st.form_submit_button("Valider")
        
    with col2:
        data_age = df[(df['Profession'] == profession) & (df['Age'] >= age[0]) & (df['Age'] <= age[1])].Age

        if valid:
            plot = sns.histplot(data_age, bins=age[1]-age[0])
            st.pyplot(plot.figure)