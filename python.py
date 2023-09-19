import streamlit as st

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

# Function to predict and display the car price
def predict_car_price():
    # Check if all input fields are filled
    if not all([car_year, car_company, car_fuel_type, car_seller_type, car_transmission_type, car_owner_type, car_mileage, car_engine]):
        st.warning("Please fill in all the car model features before predicting the price.")
    else:
        # Replace this placeholder with your actual prediction logic or ML model
        # Here, we are using a simple formula as a placeholder
        price = 100000 + (int(car_year) * 20) + (int(car_company) * 50)
        # Ensure the predicted price falls within the range of 100,000 to 300,000
        price = max(100000, min(price, 300000))
        st.write("Predicted Price of the Car is $", price)

# Create a button to trigger the car price prediction
if st.button("Predict The Car Price"):
    predict_car_price()

# Footer
st.markdown("---")
st.write("Designed and Developed by Piyush Batra")

# Footer
st.markdown("---")
st.write("Designed and Developed by Piyush Batra")
