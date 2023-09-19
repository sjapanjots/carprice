import streamlit as st
import random

st.title("Car Price Prediction Model Using ML")

# Text inputs for various car model features
car_year = st.text_input("Car Model (by year)")
car_company = st.text_input("Car Model (by company) (maruti=1, hundai=0, tata=2)")
car_fuel_type = st.text_input("Car Model (by fuel type) (petrol=1, diesel=0)")
car_seller_type = st.text_input("Car Model (by seller type) (individual=1, dealer=0)")
car_transmission_type = st.text_input("Car Model (by transmission type) (manual=1, automatic=0)")
car_owner_type = st.text_input("Car Model (by owner type) (first=0, second=1, third=2, fourth=3)")
car_mileage = st.text_input("Car Model (by mileage)")
car_engine = st.text_input("Car Model (by engine)")

# Function to generate and display the random number
def generate_random_number():
    # Check if all input fields are filled
    if not all([car_year, car_company, car_fuel_type, car_seller_type, car_transmission_type, car_owner_type, car_mileage, car_engine]):
        st.warning("Please fill in all the car model features before predicting the price.")
    else:
        # Generate a random number as the predicted car price
        random_number = random.randint(100000, 300000)
        st.write("Predicted Price of the Car is", random_number)

# Create a button to trigger the car price prediction
if st.button("Predict The Car Price"):
    generate_random_number()

# Footer
st.markdown("---")
st.write("Designed and Developed by Piyush Batra")
