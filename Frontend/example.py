import streamlit as st
#DISPLAYING TEXT

# st.write("hello.python")
# st.title("welcome to GeP protech")# the largest fonts(H1)
# st.header("we offer trainig in the following courses")# H2
# st.subheader("python, data scince,AL, ML,")# H3
# st.text("python is a programming langugae")# normal text
# st.markdown("*python is a programming language that let you work quickly and intergrade system more effectively*")
# st.caption("wait.....")

# #DISPLAY DATA
# import pandas as pd
# import numpy as np

# student_data={
#     "name":["john","jane","jack","bob"],
#     "age":[20,22,19,21],
#     "grade":["A","B","A", "C"]
# }

# df=pd.DataFrame(student_data)
# st.header("student info")
# st.dataframe(df)
# st.table(df)

# #DISPLAYING MEDIA AND IMAGES
# # st.image("https://gepprotech.com/assets/certificate-C_HL_of4.jpeg")
# # st.video("https://gepprotech.com/assets/advert-HO9yGe2p.mp4")

# #DISPLAYING INTERACTIVE WIDGETS
# #TEXT INPUT
# name=st.text_input("enter your name")
# st.write(f"Hello, {name}!")
# st.write(" welcome to GeP protech academy")
# if name: 
#        st.success("nice to have you here")

# #NUMBERS INPUT SLIDERS
# age=st.slider("enter your age",min_value=0, max_value=120, value=18, step=1)
# st.write(f"you are {age} yers old")
# score=st.slider("enter your score",min_value=0, max_value=100, value=50, step=1)
# if score >= 70:
#     st.success("congratulations")
#     st.balloons()
# elif score >= 50:
#     st.write("you need to sit up")
# else:
#     st.error("bellow average,don't gve up, ")

#     #BUTTONS

# #st.button("click me")
# #st.selectbox("choose your course",["python","data science","AI","ML"])
# #st.multiselect("choose your course",["python","data science","AI","ML"])
# st.checkbox("I agree to the terms and conditions")
# import datetime
# import time
# with st.form("my_form"):
#     st.write("user info")
#     name=st.text_input("enter your name")
#     email=st.text_input("enter your email")
#     birthday=st.date_input("enter your birthday")
#     check=st.checkbox("I agree to the terms and conditions")
#     submitted=st.form_submit_button("submit")

# if check:
#     if submitted:
#         with st.spinner("please wait..."):
#             time.sleep(5)
#             st.ballons()
#             st.success("welcome to GeP protech academy")

#USER INFO FORM
st.write("user info")
age=st.number_input("enter your age")
email=st.text_input("enter your email")
student_class=st.selectbox("choose your class",["class1","class2","class3","class4"])


if age<20:
    st.error("you are not eligible to vote")
else:
    st.success("you are eligible to vote")
if student_class in ["class1", "class2"]:
    st.warning("you can't use a pen")
else:
    st.success("you can use a pen")  

with st.sidebar:
    st.header("GeP protech academy")
    st.markdown("*learn,earn and lead*")
    st.markdown("*_________*")
    st.subheader("session stats")
    col1,col2=st.columns(2)
    with col1:
        st.subheader("massages")
        st.write("1")
    with col2:
        st.subheader("total")
        st.write("2")
st.chat_input("hello, how are you?")