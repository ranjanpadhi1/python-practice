import streamlit as st
import pandas as pd


st.title('Widget demo!')

name = st.text_input('Enter your Name:')

if name:
    age = st.slider('Select your age', 0, 100, 0)

if name and age:
    st.write(f'Hello {name}! You are {'18+ and eligible' if int(age) >= 18 else ' < 18 & not eligible'} !')    

    if age >= 18:
        language = st.selectbox('Select your favorite Language:', ['', 'Python', 'Java', 'Go'])

        if language:
            st.write('Great! you are ready to start your {language} journey...')
            file = st.file_uploader('Select a CSV file:', type='csv')

            if file:
                csv_data = pd.read_csv(file)
                st.write(csv_data)
                
            
        

