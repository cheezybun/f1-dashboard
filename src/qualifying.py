import streamlit as st 
from pathlib import Path
import base64

def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

def qualifying_cs():
    

    # fonts-style preset
     # font-style
    font_url = '''
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Syne:wght@700;800&display=swap" rel="stylesheet">
    '''
    st.markdown(f"{font_url}",unsafe_allow_html=True)

    # fonts-style preset
    style = '''
    <style>
    html, body, [class*="css"] {
        font-family: syne; 
        
    }

    </style>
    '''
    st.markdown(style,unsafe_allow_html=True)

    
    st.markdown('''<center><h4 style="font-family:syne;font-weight:900;">Analysis</h4></center>''',unsafe_allow_html=True)
    st.markdown('***')
    st.sidebar.markdown('***')

    
    cols = st.columns([3.5,4])
    cols[0].image('./assets/f1.png')
    info = '''
    "Here is a Analysis portal directly taking you into the Team Paddocks giving you a deeper look into the most constructors wins,most driver titles,number of grandprix and much more."
    '''
    cols[1].markdown(f'''<h3 style="font-family:syne">For Formula One fans,<br> <span style='font-size:22px;'>{info}</span></h3>''',unsafe_allow_html=True)
    
    

    st.markdown('***')
    st.markdown('''<center><span style="font-family:syne;font-weight:800; font-size:25px">Analysis</span></center>''',unsafe_allow_html=True)
    st.markdown('***')
    st.markdown(f'''<span style="font-family:syne; font-size:25px">Constructors championship Ranking 2022<sub style='font-size:15px'>(<img src='data:image/png;base64,{img_to_bytes('./assets/checkered-flag.png')}' class='img-fluid' width=25> completed)</sub></span>''',unsafe_allow_html=True)
    

    # race schedule
    st.image('./assets/Home/1.png')
    st.markdown('''<span style="font-family:syne; font-size:25px">Constructors championship Ranking-2021 & 2020</span>''',unsafe_allow_html=True)
    
    # session select - GP analysis
    cols = st.columns(2)
    cols[0].image('./assets/Home/2.png',caption='2021')
    cols[1].image('./assets/Home/3.png',caption='2022')

    # summarise
    st.markdown('')
    st.markdown('''<span style="font-family:syne; font-size:25px">Driver - Analysis</span>''',unsafe_allow_html=True)
    cols = st.columns(2)
    cols[0].image('./assets/Home/4.png',caption='Podium Wins')
    cols[1].image('./assets/Home/5.png',caption='Titles')
    
    st.markdown('')
    st.markdown('''<span style="font-family:syne; font-size:25px">Grand Prix that hosted most number of races</span>''',unsafe_allow_html=True)
    st.image('./assets/Home/6.png')

    
    st.markdown('''<span style="font-family:syne; font-size:18px">Comparative Driver Analysis</span>''',unsafe_allow_html=True)
    cols = st.columns(2)
    exp = cols[0].expander('Country with more wins')
    exp.image('./assets/Home/7.png')
    exp = cols[1].expander('Team wise Constructors win')
    exp.image('./assets/Home/8.png')
