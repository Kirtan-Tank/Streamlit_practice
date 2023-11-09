import streamlit as st

st.header("STREAMLIT PRACTICE")

#Button
st.header('-> st.button')

if st.button('Click button'):
  st.write("Button Pressed")
else:
  st.write("Button Not yet pressed")
