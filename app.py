import streamlit as st

st.title('TITLE :- HELLO GEEKS !!')
st.header('HEADER :- HELLO GEEKS !!')
st.subheader('SUBHEADER :- HELLO GEEKS !!')
st.text('TEXT :- HELLO GEEKS !!')

st.markdown("# HI")
st.markdown("## HI")
st.markdown("### HI")
st.markdown("#### HI")

st.success("SUCCESSFULLY SUBMITTED !")
st.info("INFORMATION HAS BEEN SUBITTED !")
st.warning("WARNING")
st.error("ERROR!")

exp=ZeroDivisionError("CANNOT DIVIDE IT BY ZERO")
st.exception(exp)

st.help(ZeroDivisionError)


st.write(range(1,10))
st.write(1+2+3)

st.code('x=10\n'
            'for i in range{x}:\n'
                'print(i)\t')


if(st.checkbox("\tMALE")):
   st.write("YOU ARE A MALE")
   
if(st.checkbox("\tFEMALE")):
    st.write("YOU ARE A FEMALE")
    

radio=st.radio('RADIOBUTTOS :',{'\tOTHER','\tMALE','\tFEMALE',})
if(radio=='\tOTHER'):
    st.markdown("#### YOUR GENDER IS UNKNOWN")
elif(radio=='\tMALE'):
    st.markdown("#### YOUR ARE A MALE")
else:
    st.markdown("#### YOU ARE A FEMALE")


st.subheader("SELECT BOX")
selectbox=st.selectbox("DATA SCIENCE:",["DATA ANALYSIS","WEB SCRAPPING","MACHINE LEARNING","DEEP LEARNING","NATURAL LANGUAGE PROCESSING","COMPUTER VISION","IMAGE PROCESSING"])
st.write("YOU HAVE SELECTED:",selectbox)


st.subheader("MULTI SELECT BOX")
multiselect=st.multiselect("DATA SCIENCE:",["DATA ANALYSIS","WEB SCRAPPING","MACHINE LEARNING","DEEP LEARNING","NATURAL LANGUAGE PROCESSING","COMPUTER VISION","IMAGE PROCESSING"])
st.write("YOU HAVE SELECTED:",len(multiselect),"COURSES")

st.subheader("BUTTONS")
r=st.button("CLICK ME")
if(r):
    st.write("BUTTON CLICKED") 



st.subheader("SLIDER")
vol=st.slider("SELECT THE VOLUME",0,100,step=1)
st.write("THE VOLUME IS :",vol)

st.subheader("TEXT INPUT")
name=st.text_input("NAME :")
if(name):
    st.write("HI",name)
pss=st.text_input("PASSWORD :",type="password")
if(pss):
    if(pss=="1234"):
        st.write("WELCOME SIR")
    else:
        st.write("WRONG PASSWORD TRY AGAIN")

st.subheader("TEXT AREA")
ar=st.text_area("WRITE SOMETHING ABOUT YOURSELF :")
bt=st.button("SUBMIT")
if(bt):
    if(ar):
        st.success("TEXT SUBMITTED")
    else:
        st.error("TEXT BOX IS EMPTY")

st.subheader("INPUT NUMBER")
num=st.number_input("SELECT YOUR AGE :",18,100)
if(num in range(18,100)):
    st.write("YOUR AGE IS ",num)
else:
    st.error("WRONG INPUT")
    

st.subheader("INPUT DATE")
date=st.date_input("SELECT THE DATE :")
st.write(date)


st.subheader("INPUT TIME")
time=st.time_input("SELECT THE TIME :")
st.write(time)
