import streamlit as st 
import pandas as pd 
import numpy as np
import json
import streamlit_lottie as st_lottie
import requests
from streamlit_extras.colored_header import colored_header
from annotated_text import annotated_text
from PIL import Image
from streamlit_extras.stoggle import stoggle
from streamlit_extras.let_it_rain import rain
import matplotlib.pyplot as plt
import plotly.express as px

# Page settings
st.set_page_config(page_title="PYTHON 2 - BUSINESS IT 2", page_icon="🧡", layout="wide")

# Title & intro
st.title("PYTHON 2 - BUSINESS IT 2 :orange_heart:")
st.write(
    "We are a group of business students who are interested in the economical situation in the world. "
    "Therefore, we decided to analyze a set of data about the employment fluctuation in the USA from 1978 to 2022. "
    "Through this visualization, we hope to bring a clear vision to people about how the labor market in the USA has changed over the past decades."
)

# Group info
st.markdown("""
**Group information**
1. Ho Huynh Gia Phuc - 10624031706240317  
2. Nguyen Thanh Thuy - 103240395  
3. Nguyen Ho Huy Thong - 106240515  
4. Vu Thien Tuan - 103240493  
5. Pham Tuyet Mai - 103240500  
""")

# Animation
rain(
    emoji="🔍",
    font_size=54,
    falling_speed=5,
    animation_length="3",
)

# Section: Introduction
colored_header(
    label="Group members introduction",
    description="Get to know about our group",
    color_name="light-blue-70",
)

# Member 1
col1, col2 = st.columns(2)
with col1:
    giaphuc = Image.open("pages/1.png")
    st.image(giaphuc)
with col2:
    st.subheader("**Full name: Ho Huynh Gia Phuc (Group leader)**")
    st.write("Student ID: 106240317")
    st.write("Email: 106240317@student.vgu.edu.vn")
    st.write("Major: Business Administration (BBA)")

st.write(" ")

# Member 2
col1, col2 = st.columns(2)
with col1:
    thanhthuy = Image.open("pages/2.png")
    st.image(thanhthuy)
with col2:
    st.subheader("**Full name: Nguyen Thanh Thuy**")
    st.write("Student ID: 103240395")
    st.write("Email: 103240395@student.vgu.edu.vn")
    st.write("Major: Finance & Accounting (BFA)")

st.write(" ")

# Member 3
col1, col2 = st.columns(2)
with col1:
    huythong = Image.open("pages/4.png")
    st.image(huythong)
with col2:
    st.subheader("**Full name: Nguyen Ho Huy Thong**")
    st.write("Student ID: 106240515")
    st.write("Email: 106240515@student.vgu.edu.vn")
    st.write("Major: Business Administration (BBA)")

st.write(" ")

# Member 4
col1, col2 = st.columns(2)
with col1:
    thientuan = Image.open("pages/5.png")
    st.image(thientuan)
with col2:
    st.subheader("**Full name: Vu Thien Tuan**")
    st.write("Student ID: 103240493")
    st.write("Email: 103240493@student.vgu.edu.vn")
    st.write("Major: Business Administration (BBA)")

st.write(" ")

# Member 5
col1, col2 = st.columns(2)
with col1:
    tuyetmai = Image.open("pages/3.png")
    st.image(tuyetmai)
with col2:
    st.subheader("**Full name: Pham Tuyet Mai**")
    st.write("Student ID: 103240500")
    st.write("Email: 103240500@student.vgu.edu.vn")
    st.write("Major: Business Administration (BBA)")

# Contact form
st.markdown("---")
st.subheader("💬 Leave us your message!")
st.caption("Let us know if you have any recommendations")

contactform = """
<form action="https://formsubmit.co/106240515@student.vgu.edu.vn" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email address" required>
     <textarea name="message" placeholder="What do you think?"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contactform, unsafe_allow_html=True)

# Optional: Custom CSS
def local_css(style):
    with open(style) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
