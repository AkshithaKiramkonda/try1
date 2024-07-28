import streamlit as st
import time
import numpy as np
import pandas as pd
from PIL import Image as i
from datetime import datetime

st.set_page_config(page_title="Date Invitation",page_icon="💌")
st.title("Hello Future Husband❤")
st.subheader("R u ready to go on a date with me!!")
st.subheader("Choose the Date")
today=datetime.now().date()
date=st.date_input("Enter the date where u can dedicate the whole day for me",min_value=today.replace(day=today.day+2),max_value=today.replace(day=today.day+2))
st.write("Now u have given this day to me remember no changes r to be made",datetime.strftime(date, '%y/%m/%d'))

st.subheader("Choose the place")
place=st.selectbox("Choose the place", options = ("Home","outside"),help="choose one")
st.write("You have selected",place)

st.subheader("Choose one outfit")
option = st.selectbox("select ur options : ", options = ("Western","Traditional"), help = "choose one")
st.write("you have selected", option)

st.subheader("Example")
tab1,tab2=st.tabs(["Western","Traditional"])
with tab1:
    st.subheader("Western")
    #hid1=i.open("C:/Users/HP/OneDrive/Pictures/hid 2.jpg")
    st.image("deploy/hid2.jpg",width=400)
with tab2:
    st.subheader("Traditional")
    st.image("deploy/hid1.jpg",width =400)
st.write("The common part is u have to always look only me😂 ")

st.subheader("Quiz")
with st.form("Date"):
    col1,col2=st.columns([2,1])
with col1:
    quiz=st.date_input("Enter the most memorable day for us",help="Should be in numbers")
with col2:
    submit = st.form_submit_button("Submit")

    if submit:
        st.success("Hurrah!! u have won a Surprise Gift")
    else:
        st.error("Wrong Answer ")

with st.expander("R u ready!!"):
    tab1,tab2=st.tabs(["",""])
    with tab1:
        st.video("deploy/hid3.mp4")
    with tab2:
        st.write("")
    st.write(""""
    First ever date!!! I am sooooo sooooo excited for thiss.Let's enjoy it to the fullestttt
     """)
st.subheader("Here there is something for u")
st.audio("deploy/mine.unknown")
st.subheader("Rate ur experience")
st.slider("How did u like it",min_value=0,max_value=5)


st.balloons()
