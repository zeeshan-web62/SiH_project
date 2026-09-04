import requests
import streamlit as st


@st.cache_data(ttl=3600, show_spinner=False)
def get_terrain(latitude, longitude):

    url = (
        "https://api.open-meteo.com/v1/elevation"
        f"?latitude={latitude}"
        f"&longitude={longitude}"
    )

    try:

        response = requests.get(url, timeout=(3, 6))
        response.raise_for_status()

        data = response.json()

        elevation = data["elevation"][0]

        return {
            "elevation": elevation
        }

    except Exception:

        return None
