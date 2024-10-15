import streamlit as st

st.title("Feedback")

st.write("Please provide your feedback below:")
st.text_area("", "Type your feedback here...")

st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
st.button("Submit")
st.markdown("</div>", unsafe_allow_html=True)

st.text("")
st.text("")

exp = Warning("This site is currently under construction. Some features may not be available.")
st.exception(exp)