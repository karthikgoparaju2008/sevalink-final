import streamlit as st
import pandas as pd
import os
from datetime import datetime
import random

# 1. Page Config
st.set_page_config(page_title="SevaLink", page_icon="♻️", layout="wide")

# 2. File Setup (Simulated Database)
if not os.path.exists('donations.csv'):
    df = pd.DataFrame(columns=['Date', 'Name', 'Phone', 'Address', 'Weight_Kg', 'Meals_Funded'])
    df.to_csv('donations.csv', index=False)

# 3. Sidebar
st.sidebar.title("SevaLink ♻️")
role = st.sidebar.selectbox("Choose Role", ["Donor", "Admin"])

# 4. Donor Interface
if role == "Donor":
    st.title("Donate Newspapers, Fund Education 🎓")
    st.write("Turn your waste into wisdom for a student.")
    
    with st.form("donation_form"):
        name = st.text_input("Your Name")
        phone = st.text_input("Phone Number")
        address = st.text_area("Pickup Address")
        photo = st.file_uploader("Upload Photo", type=['jpg', 'png'])
        
        weight_est = 0
        if photo:
            weight_est = random.randint(3, 12)
            st.info(f"🤖 AI estimates this pile is approx {weight_est} kg")
            
        submitted = st.form_submit_button("Schedule Pickup")
        
        if submitted and name:
            meals = int((weight_est * 12) / 24)
            # Save Data
            new_data = pd.DataFrame({
                'Date': [datetime.now().strftime("%Y-%m-%d %H:%M")],
                'Name': [name],
                'Phone': [phone],
                'Address': [address],
                'Weight_Kg': [weight_est],
                'Meals_Funded': [meals]
            })
            new_data.to_csv('donations.csv', mode='a', header=False, index=False)
            st.success(f"Yay! {name}, you funded {meals} meals! 🥗")

# 5. Admin Interface
elif role == "Admin":
    st.title("Admin Dashboard 🚚")
    pwd = st.sidebar.text_input("Password", type="password")
    
    if pwd == "seva123":
        st.success("Login Successful")
        try:
            data = pd.read_csv('donations.csv')
            st.dataframe(data)
        except:
            st.write("No data yet.")
    elif pwd:
        st.error("Wrong Password")
