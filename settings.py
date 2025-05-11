import streamlit as st

def show_settings():
    st.title("Settings")

    st.subheader("GNSS Device Configuration")
    port = st.text_input("Serial Port", value="/dev/ttyACM0")
    baud_rate = st.number_input("Baud Rate", min_value=1200, max_value=115200, value=9600)

    if st.button("Save Configuration"):
        st.success(f"Configuration saved: Port={port}, Baud={baud_rate}")