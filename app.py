import streamlit as st
import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px
import matplotlib.pyplot as pit

st.set_page_config(layout='wide', page_title='My age')

# html variable
html = '''
<html>
    <head>
        <title> this is html app </title>
    </head>
    <body>
        <h1> THIS LONG TEXT! </h1>
        <br>
        <hr>
        <h3> small TEXT </h3>
    </body>
</html>
'''


#global variable
url = "https://www.youtube.com/watch?v=XyEOEBsa8I4"

#data appdd
df = pd.read_csv('./data/data.csv')

with open('./com.html', 'r', encoding='utf-8') as f:
    filehtml = f.read()
    f.close()

st.title('This is my first webapp!')
col1, col2 = st.columns((4,1))

st.markdown(html, unsafe_allow_html=True)

with col1:
    with st.expander('Content1...'):
        st.subheader('Content1...')
        st.video(url)

    with st.expander('Content2_image...'):
        st.subheader('Content2_image...')
        st.image('./images/catdog.jpg')
        st.write('<h1> this is new title </h1>', unsafe_allow_html=True )
        st.markdown(html, unsafe_allow_html=True)


    with st.expander('Content3_html...'):
        st.subheader('Content2_image...')
        import streamlit.components.v1 as htmlviewer
        htmlviewer.html(filehtml, height=800)


with col2:
    with st.expander('Tips...'):
        st.subheader('Tips...')