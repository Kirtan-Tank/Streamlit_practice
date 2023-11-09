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

st.markdown(""" # _This is italic h1 markdown heading_ 
- ## _This is italic h2 markdown heading_ 
- ### _This is italic h3 markdown heading_ """)

st.markdown(" Cool guy emoji :sunglasses:")

#using html tags inside markdown
st.markdown(""" The emojis are separated by break tag <br> :earth: <br> :moon: <br> :fire: <br> :water: <br>""")
