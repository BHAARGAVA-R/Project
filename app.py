import streamlit as st
from utils.api_client import GNSSApiClient
import folium
from streamlit_folium import folium_static

# Initialize API Client
client = GNSSApiClient()

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Real-Time Location", "History", "Settings"])

if page == "Real-Time Location":
    st.title("🌍 Real-Time GNSS Dashboard")

    # Fetch latest location
    location = client.get_latest_location()

    lat = location["latitude"]
    lon = location["longitude"]

    st.metric("Latitude", f"{lat:.6f}")
    st.metric("Longitude", f"{lon:.6f}")

    # Display Map
    m = folium.Map(location=[lat, lon], zoom_start=16)
    folium.Marker([lat, lon], popup="Current Location").add_to(m)

    st.subheader("Location Map")
    folium_static(m)

elif page == "History":
    from pages.history import show_history
    show_history()

elif page == "Settings":
    from pages.settings import show_settings
    show_settings()