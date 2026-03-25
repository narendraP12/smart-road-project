import streamlit as st
import folium
from streamlit_folium import st_folium
import random
import time

# --- Page Config ---
st.set_page_config(page_title="Smart Road Planner", layout="wide")

# --- Session State (Taki route gayab na ho) ---
if 'route_coords' not in st.session_state:
    st.session_state.route_coords = None

st.title("🗺️ Smart Rural Road: Interactive GIS Map")

# Sidebar Menu
menu = ["Road Planning (GIS)", "Project Overview"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Road Planning (GIS)":
    col1, col2 = st.columns([1, 2])

    with col1:
        st.subheader("Selection & Logic")
        village = st.selectbox("Select Village", ["Piregur", "Mame Retm"])
        
        # FIND ROUTE BUTTON
        if st.button("Find Optimized Route"):
            with st.spinner('Calculating...'):
                # Yeh aapke optimized path ke coordinates hain (Lat, Lon)
                # Aap inhen apne area ke hisab se badal sakte hain
                path = [
                    [21.1458, 79.0882], 
                    [21.1490, 79.0910], 
                    [21.1520, 79.0940], 
                    [21.1560, 79.1000]
                ]
                st.session_state.route_coords = path
                st.success("✅ Optimized Route Found (Red Line)!")

    with col2:
        # --- INTERACTIVE MAP SETUP ---
        # Starting point (Nagpur region example)
        m = folium.Map(location=[21.1458, 79.0882], zoom_start=14)

        # AGAR route find ho gaya hai, toh RED LINE aur MARKERS draw karein
        if st.session_state.route_coords:
            # 1. Red Line Draw Karna
            folium.PolyLine(
                locations=st.session_state.route_coords,
                color="red",
                weight=6,
                opacity=0.8,
                tooltip="Optimized Path"
            ).add_to(m)

            # 2. Start aur End Markers add karna
            folium.Marker(st.session_state.route_coords[0], 
                          popup="Start", icon=folium.Icon(color='green')).add_to(m)
            folium.Marker(st.session_state.route_coords[-1], 
                          popup="End", icon=folium.Icon(color='red')).add_to(m)

        # Map ko display karna (Interactive Mode)
        st_folium(m, use_container_width=True, height=500)

# Footer
st.markdown("---")
st.caption("Developed with Streamlit-Folium for GIS Visualization")
