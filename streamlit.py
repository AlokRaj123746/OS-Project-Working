import streamlit as st

st.title("🚀 Advanced Disk Scheduling Simulator")

req_str = st.text_input("Enter disk requests", "82, 170, 43, 140, 24, 16, 190")
head = st.number_input("Starting head position", 0, 500, 50)
disk_size = st.number_input("Disk Size (Cylinders)", 100, 1000, 200)
