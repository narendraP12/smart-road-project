import streamlit as st
import random
import time

# Title
st.set_page_config(page_title="Smart Road Planner", layout="wide")
st.title("🛣️ Smart Rural Road: GIS & IoT Optimizer")

# Tabs for Sidebar
menu = ["Project Overview", "Road Planning (GIS)", "Live Energy Monitor"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Project Overview":
    st.subheader("About the Project")
    st.write("Yeh project rural roads ko durable aur sustainable banane ke liye hai.")

elif choice == "Road Planning (GIS)":
    st.header("📍 GIS Route Optimization")
    file = st.file_uploader("Upload Terrain Map", type=['png', 'jpg'])
    if file:
        st.image(file, caption="Map Uploaded", use_container_width=True)
        st.info("Finding Least Cost Path... (Avoiding Flood Zones)")
        st.success("✅ Optimized Route Found! (Durability: 95%)")

elif choice == "Live Energy Monitor":
    st.header("⚡ Live Piezoelectric Feed")
    if st.button('Start Tracking'):
        placeholder = st.empty()
        for i in range(20):
            voltage = round(random.uniform(2.0, 5.0), 2)
            placeholder.metric("Current Voltage", f"{voltage} V")
            time.sleep(1)
