import streamlit as st
import datetime



if "name" not in st.session_state:
    st.session_state.name = ""


st.write("### Prüfungsdatum")
datum=st.text_input("Gib dein Prüfungsdatum ein (Format: Tag.Monat.Jahr Bsp.: 01.08.2022):", key="name")

#d = {'Index Title': ['Word-Vorlage', 'Teilnehmenden-Listen'],'': [ "", ""]}
#df = pd.DataFrame(d).set_index('Index Title')

word_str=""
tn_str=""
verbleibend_word=""
verbleibend_tn=""
verbleibend_word_support=""
word_str_support=""

if datum!="":
    today=datetime.datetime.now().date()
    datum=datetime.datetime.strptime(datum,"%d.%m.%Y")

    word_date=(datum-datetime.timedelta(weeks=8)).date()
    word_str=word_date.strftime("%d.%m.%Y")
    
    tn_date=(datum-datetime.timedelta(weeks=4)).date()
    tn_str=tn_date.strftime("%d.%m.%Y")
    
    verbleibend_word=(word_date-today).days
    verbleibend_word=f"{verbleibend_word} Tage"

    word_date_support=(datum-datetime.timedelta(weeks=5)).date()
    word_str_support=word_date_support.strftime("%d.%m.%Y")

    verbleibend_word_support=(word_date_support-today).days
    verbleibend_word_support=f"{verbleibend_word_support} Tage"

    verbleibend_tn=(tn_date-today).days
    verbleibend_tn=f"{verbleibend_tn} Tage"



st.write("### Tagesgeschäft")
st.write(f"#### Word-Vorlage: {word_str}         (verbleibende Zeit: {verbleibend_word})",key="word")
st.write(f"#### TN-Liste: {tn_str} (verbleibende Zeit: {verbleibend_tn})",key="tn")  

st.write("")
st.write("### Support-Projekt")
st.write(f"#### Word-Vorlage: {word_str_support}         (verbleibende Zeit: {verbleibend_word_support})",key="word")
st.write(f"#### TN-Liste: {tn_str} (verbleibende Zeit: {verbleibend_tn})",key="tn") 

