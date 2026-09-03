import streamlit as st
#DISPLAYING TEXT

st.write("hello.python")
st.title("welcome to GeP protech")# the largest fonts(H1)
st.header("we offer trainig in the following courses")# H2
st.subheader("python, data scince,AL, ML,")# H3
st.text("python is a programming langugae")# normal text
st.markdown("*python is a programming language that let you work quickly and intergrade system more effectively*")
st.caption("wait.....")

#DISPLAY DATA
import pandas as pd
import numpy as np

student_data={
    "name":["john","jane","jack","bob"],
    "age":[20,22,19,21],
    "grade":["A","B","A", "C"]
}

df=pd.DataFrame(student_data)
st.header("student info")
st.dataframe(df)
st.table(df)

#DISPLAYING MEDIA AND IMAGES
# st.image("https://gepprotech.com/assets/certificate-C_HL_of4.jpeg")
# st.video("https://gepprotech.com/assets/advert-HO9yGe2p.mp4")

#DISPLAYING INTERACTIVE WIDGETS
#TEXT INPUT
name=st.text_input("enter your name")
st.write(f"Hello, {name}!")
st.write(" welcome to GeP protech academy")
if name: 
       st.success("nice to have you here")
