import streamlit as st
# import ezsheets
# import pandas   
from login_signup import login_signup # import the login_signup class from the login_signup.py file

# Connect to the Google Sheets API
# ss = ezsheets.Spreadsheet('152M9yVlljFVDf5Nnd2oBjWfvxf5Sfy2n2H7Sz5__1F4')

st.title("Login or Sign Up") # Set the title of the page
st.sidebar.title("Project CMS") # Set the Side menu
page = st.sidebar.radio("## Menu", ["Login", "Create an account"])  # Create a radio button for page selection
              
# Page routing logic
if page == "Login":
    login_signup.login()
elif page == "Create an account":
    login_signup.create_an_account()
elif page == "forgot_password":
    login_signup.forgot_password()