import streamlit as st
#DISPLAYING TEXT

#MAIN PAGE
st.title("💬Chat With GePAI")#the largest fonts(H1)
st.divider()


#USER MASSAGE
st.info(
    "👾Hello i am suffering from high blood presure what can i do"
)
st.markdown("Hello there! i am really sorry to hear that you are suffering from high blood pressure. it is a serious condition, buy the good news is that there is a lot you can do to manage it and improve your health \n\n since i am an AI,i cannot give you medical advice, and it is super important to talk to a doctor or  a health professional about your specific situation.They can give you a proper diagnosis and create a persionalised plan for you.\n\n However, based on general understanding of heart health and risk factors,here are common steps that otfen helps in managing high blood pressure:\n\n1. Talk to your doctor:This is the most important step! A doctor can confirm your diagnosis,discuss medical option if needed,and guide you on the best course of action for your health\n2. Healthy Eating:\n                -Reduce Sodium(salt):this is often a big one! Tomuch salt can raise blood pressure.Try to limit procces foods,\ncanned goods,and salty snacks.Cook more at home where you control the ingredients.\n                -Eats more fruits and vegetabless:They are packed with nutrients and fiber, and naturally low in sodium. ")
 
st.divider()
st.divider()

massage=st.chat_input("Massage GePAI")
if massage:
    st.write("you:",Massage)

#SIDEBAR
with st.sidebar:
    st.header("🌱GePAI")
    st.markdown("*learn,earn and lead*")
    st.divider()
    st.subheader("📊Session stats")
    col1,col2=st.columns(2)
    with col1:
        st.subheader("Massages")
        st.write("1")
    with col2:
        st.subheader("Total")
        st.write("2")
    st.divider()
    st.subheader("⚙Controls")
    
    #BUTTON
    st.write("Accents")
    st.selectbox("choose your accent",["nigeria","cameroon","china","zimbabui","chad","maxico","south afica"])
    st.write("Model Temperature")
    temperature=st.slider(
        "enter temperature",
        min_value = 0.00, 
        max_value=2.00,
        value=1.20,
        step=0.01
        )


        
