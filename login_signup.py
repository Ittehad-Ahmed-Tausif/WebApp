import streamlit as st
import re
import time
from datetime import datetime
import ezsheets


class login_signup:

    def login():
        st.text("")
        username = st.text_input("Email or phone number")
        password = st.text_input("Password", type="password")

        st.text("")
        col1, col2, col3 = st.columns([2,2.3,2])
        with col2:
            col2_1, col2_2 = st.columns([1, 2]) 
            with col2_1:
                login_button = st.button("Login") 
            with col2_2:
                forgot_password = st.button("Forgot Password")
                
        if login_button:
            if login_signup.verify_login(username, password):
                st.success("Congratulations! You have successfully logged in.")
                
                # Redirect to the main application page 
                # need to be done

            else:
                st.error("Invalid username or password. Please try again.")

        if forgot_password:
            # Redirect to forgot password page
            st.write("Redirecting to forgot password page...")

            time.sleep(1)
            # page == "forgot_password"
            
            login_signup.forgot_password()

    def verify_login(username, password):
        ss = ezsheets.Spreadsheet('152M9yVlljFVDf5Nnd2oBjWfvxf5Sfy2n2H7Sz5__1F4') # the spreadsheet ID
        sheet = ss[0]  # the first sheet

        emails = sheet.getColumn(7)[4:]  # Column G, starting from row 5
        phones = sheet.getColumn(8)[4:]  # Column H, starting from row 5
        passwords = sheet.getColumn(9)[4:]  # Column I, starting from row 5

        for email, phone, pwd in zip(emails, phones, passwords):
            if (username == email or username == phone) and password == pwd:
                return True
        return False

    def create_an_account():
        first_name = st.text_input("First Name") 
        last_name = st.text_input("Last Name")
        dob = st.date_input("Date of Birth", datetime.today())
        gender = st.radio("Gender", ("Other", "Male", "Female"), horizontal=True)   
        address1 = st.text_input("Address Line 1")         
        address2 = st.text_input("Address Line 2") 
        phone_number = st.text_input("Phone Number")        
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        retype_password = st.text_input("Retype Password", type="password")

        # Create the checkbox and markdown in a single line using columns
        col1, col2 = st.columns([0.05, 1])  # Adjust the width ratios as needed

        # Checkbox in the first column
        with col1:
            terms_privacy = st.checkbox("")
        with col2:
            st.markdown('I acknowledge that I have read and agree to the [Terms & Conditions](https://example.com/terms) and [Privacy Policy](https://example.com/privacy). By using this service, I consent to the collection, use, and sharing of my data as outlined in the policies.', unsafe_allow_html=True)

        st.text("")

        # a button to create an account 
        col1, col2, col3 = st.columns([2,2,1])
        with col2:
            create_account_button = st.button("Create an account")

        if create_account_button:
            if not re.match(r"^[A-Za-z][A-Za-z ]*$", first_name):
                    st.warning("First name must contain only characters.")
            elif not re.match(r"^[A-Za-z][A-Za-z ]*$", last_name):
                st.warning("Last name must contain only characters.")
            elif not address1:
                st.warning("Address Line 1 must be filled.")
            elif phone_number.isnumeric() == False:
                st.warning("Phone number must contain only digits.")
            elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                st.warning("Invalid email address. Please enter a valid email address.")
            elif len(password) < 8:
                st.warning("Password must be at least 8 characters long.")
            else:
                count = 0
                if any(c.isupper() for c in password):
                    count += 1
                if any(c.islower() for c in password):
                    count += 1
                if any(c.isdigit() for c in password):
                    count += 1
                if any(c in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~" for c in password):
                    count += 1
                
                if count < 3:
                    st.warning("Password must contain at least three of the following: uppercase letters [A], lowercase letters [a], digits [0], special characters [@].")
                elif password != retype_password:
                    st.warning("Passwords do not match. Please retype the password.")
                elif not terms_privacy:
                    st.warning("You must accept the terms & conditions and privacy policy to proceed.")
                else:
                    try:
                        ss = ezsheets.Spreadsheet('152M9yVlljFVDf5Nnd2oBjWfvxf5Sfy2n2H7Sz5__1F4')
                        sheet = ss['Login Credentials']

                        sheet.updateRow((sheet.rowCount + 1), [first_name, last_name, dob.strftime('%Y-%m-%d'), gender, address1, address2, phone_number, email, password, datetime.now().strftime('%d-%m-%Y  %H:%M:%S')])
                        st.success("Congratulations! You have successfully created an account.")
                    
                    except Exception as e:
                        st.error(f"An error occurred while creating the account: {e}")
                
    def forgot_password():
        st.warning("This site is currently under construction. Some features may not be available.")
    
    #checked