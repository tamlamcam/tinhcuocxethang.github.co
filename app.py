import streamlit as st
import pandas as pd


st.set_page_config(page_title="Tính giá thuê xe", layout="wide")

st.title("🚗 Phần mềm tính giá thuê xe")

# =========================
# Khởi tạo dữ liệu xe
# =========================
if "cars" not in st.session_state:
    st.session_state.cars = {
        "Toyota Innova 2019": 11000000,
        "Toyota Innova 2020": 12000000,
        "Toyota Innova 2021": 13000000,
        "Toyota Innova 2023": 14000000,
        "Toyota Fortuner 2021": 18000000,
        "Toyota Fortuner 2022": 22000000,
        "Toyota Camry2.0G 2023": 23000000,
        "Toyota Camry2.5Q 2020": 22000000,
        "Ford Transit 2024": 17000000,
        "Ford Everest 2023": 20000000,
        "KIA Carnival 2021": 20000000,
        "KIA Carnival 2022": 23000000,
        "KIA Carnival 2023": 26000000,
        "Mazda Cx8 2020": 21500000,
        "Mitsubishi Xpander 2020": 10000000
    

    }

# =========================

# 3. NHẬP DỮ LIỆU
# =========================
st.subheader("📋 Bảng định mức theo xe")

data = {
    "Xe": ["Innova", "Fortuner", "Camry", "Carnival"],
    "Nhiên liệu": ["Xăng", "Dầu", "Xăng", "Dầu"],
    "Định mức": [12, 12, 15, 13]
}

df_car = pd.DataFrame(data)

st.table(df_car)
st.subheader("📊 Nhập thông tin tính toán")

car_choice = st.selectbox("Loại xe muốn thuê", list(st.session_state.cars.keys()))
car_price = st.session_state.cars[car_choice]

fuel_price = st.number_input("Giá nhiên liệu (VNĐ/lít)", value=25000)
consumption = st.number_input("Định mức (lít/100km)", value=10.0)
km_month = st.number_input("Số km hàng tháng", value=2000)

work_days = st.selectbox("Số ngày công", [22, 26])
maintenance = st.selectbox("Tiền bảo dưỡng", [2000000, 3000000])

# =========================
# Tính toán
# =========================
fuel_cost = (fuel_price * consumption * km_month) / 100

if work_days == 22:
    driver_salary = 10000000
else:
    driver_salary = 12000000

total_price = 1.1 * (car_price + fuel_cost + driver_salary + maintenance)

# =========================
# Hiển thị kết quả
# =========================
st.subheader("📈 Kết quả")

result = pd.DataFrame({
    "Khoản mục": [
        "Giá khoán (Giá xe)",
        "Giá nhiên liệu hao tổn",
        "Lương tài xế",
        "Tiền bảo dưỡng",
        "Giá thuê xe"
    ],
    "Giá trị (VNĐ)": [
        car_price,
        fuel_cost,
        driver_salary,
        maintenance,
        total_price
    ]
})

st.table(result.style.format({"Giá trị (VNĐ)": "{:,.0f}"}))
