import streamlit as st

st.title('Contact Us')
st.text('')
st.text('')
st.markdown('#### About the Developer ')
st.markdown("""
<div style="text-align: justify;">
This application was developed by <b>Ittehad Ahmed Tausif</b>. As a passionate software developer, Ittehad strives to create solutions that are not only functional but also user-friendly. With a strong foundation in programming and a commitment to continuous learning, Ittehad has developed this application to meet the specific needs of its users, ensuring a smooth and seamless experience.
</div>
""", unsafe_allow_html=True)

st.text('')

st.markdown("""
<div style="text-align: justify;">
For inquiries or feedback, feel free to reach out and share your thoughts. Ittehad values user input and is dedicated to improving the application based on real user experiences.
</div>
""", unsafe_allow_html=True)

st.text('')
st.text('')
st.text('')


exp = Warning("This site is currently under construction. Some features may not be available.")
st.exception(exp)