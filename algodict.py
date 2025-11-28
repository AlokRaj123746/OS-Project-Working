import streamlit as st

def parse_requests(req_str):
    try:
        req_list = list(map(int, req_str.replace(" ", "").split(",")))
        return req_list
    except:
        st.error("❌ Invalid input! Enter numbers separated by commas.")
        return None

st.title("🚀 Advanced Disk Scheduling Simulator")
req_str = st.text_input("Enter disk requests", "82, 170, 43, 140, 24, 16, 190")
head = st.number_input("Starting head position", 0, 500, 50)
disk_size = st.number_input("Disk Size (Cylinders)", 100, 1000, 200)

algorithms = {}
