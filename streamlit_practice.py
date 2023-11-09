import streamlit as st

st.title("STREAMLIT PRACTICE")

#Button
st.header('-> st.button')

if st.button('Click button'):
  st.write("Button Pressed")
else:
  st.write("Button Not yet pressed")

st.subheader("This is a subheader")
st.text("This is text cannot change font")

st.markdown("# _This is italic h1 markdown heading_")
