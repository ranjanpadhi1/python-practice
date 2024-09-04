import pandas as pd
import streamlit as st
import numpy as np

#Title and text
st.title('Streamlit Demo')
st.write('Welcome to the first Streamlit application')

#Grid
st.write('Grid Data')
# data = pd.DataFrame(columns=['Name', 'Age', 'Email'], data=[['Ranjan', 33, 'ranjan@gmail.com'], ['Deepak', 36, 'deepak@gmail.com']])

data = pd.DataFrame({
    'Name' : ['Ranjan', 'Deepak'],
    'Age' : [33, 36],
    'Email' : ['ranjan@gmail.com', 'deepak@gmail.com']
})
st.write(data)

#Charts
st.write('Chart Data')
chart_data = pd.DataFrame(np.random.randn(20, 2), columns=['Ranjan', 'Deepak'])
st.line_chart(chart_data)

