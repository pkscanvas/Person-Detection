#!/usr/bin/env python
# coding: utf-8


import streamlit as st
from PersonDetector import person_detector
from PIL import Image
st.title("Detecting Humans in scene")
st.header("Havells Assignment 2")
st.text("Upload an image")

uploaded_file = st.file_uploader("Choose a jpg file ...", type="jpg")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='File uploaded.', use_column_width=True)
    st.write("")
    st.write("Classifying...")
    label = person_detector(image)
    if label == 0:
        # st.write("No Person Detected")
        st.markdown(""" <style> .font {
        font-size:50px ; font-family: 'Cooper Black'; color: #FF9633;} 
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">No Person Detected!</p>', unsafe_allow_html=True)
    else:
        # st.write("Person Detected")
        st.markdown(""" <style> .font {
        font-size:50px ; font-family: 'Cooper Black'; color: #FF9633;} 
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">Person Detected!</p>', unsafe_allow_html=True)

