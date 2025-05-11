import sqlite3
import pandas as pd
import streamlit as st

def show_history():
    st.title("GNSS Data History")

    conn = sqlite3.connect("gnss_data.db")
    df = pd.read_sql_query("SELECT * FROM gnss_log ORDER BY timestamp DESC LIMIT 100", conn)

    st.dataframe(df)

    if not df.empty:
        st.map(df[['latitude', 'longitude']])
    else:
        st.info("No historical data found.")