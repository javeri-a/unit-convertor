import streamlit as st

def convert_units(value, from_unit, to_unit, category):
    conversions = {
        "Length": {
            "Meter": 1, "Kilometer": 0.001, "Centimeter": 100, "Millimeter": 1000,
            "Mile": 0.000621371, "Yard": 1.09361, "Foot": 3.28084, "Inch": 39.3701
        },
        "Weight": {
            "Kilogram": 1, "Gram": 1000, "Milligram": 1000000, "Pound": 2.20462,
            "Ounce": 35.274
        },
        "Temperature": {
            "Celsius": lambda x: x, "Fahrenheit": lambda x: (x * 9/5) + 32,
            "Kelvin": lambda x: x + 273.15
        },
        "Speed": {
            "Meter per second": 1, "Kilometer per hour": 3.6, "Mile per hour": 2.23694,
            "Foot per second": 3.28084
        }
    }
    
    if category == "Temperature":
        return conversions[category][to_unit](value) if from_unit == "Celsius" else value
    else:
        return value * conversions[category][to_unit] / conversions[category][from_unit]

st.title("Universal Unit Converter")

categories = ["Length", "Weight", "Temperature", "Speed"]
category = st.selectbox("Select Conversion Category:", categories)

units = {
    "Length": ["Meter", "Kilometer", "Centimeter", "Millimeter", "Mile", "Yard", "Foot", "Inch"],
    "Weight": ["Kilogram", "Gram", "Milligram", "Pound", "Ounce"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
    "Speed": ["Meter per second", "Kilometer per hour", "Mile per hour", "Foot per second"]
}

from_unit = st.selectbox("From Unit:", units[category])
to_unit = st.selectbox("To Unit:", units[category])
value = st.number_input("Enter Value:", value=0.0, format="%.2f")

if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit, category)
    st.success(f"{value} {from_unit} is equal to {result:.2f} {to_unit}")
