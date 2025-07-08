import streamlit as st
from datetime import timedelta

st.set_page_config(page_title="Corridômetro", layout="centered")

# Add logo
st.image("https://github.com/BacalhauNaBrisa/corridometro/raw/main/assets/logo.png", use_container_width=True)
st.title("🏃 Corridômetro")

# Updated tab names in Portuguese
tab1, tab2, tab3 = st.tabs(["🕒 Velocidade", "📏 Distância", "⏱️ Tempo"])

def parse_time_input(time_str):
    try:
        h, m, s = map(int, time_str.strip().split(":"))
        return timedelta(hours=h, minutes=m, seconds=s).total_seconds()
    except:
        return None

def convert_distance_to_meters(distance, unit):
    if unit == "kilometers":
        return distance * 1000
    elif unit == "meters":
        return distance
    elif unit == "miles":
        return distance * 1609.34

def convert_meters_to_distance(meters, unit):
    if unit == "kilometers":
        return meters / 1000
    elif unit == "meters":
        return meters
    elif unit == "miles":
        return meters / 1609.34

def convert_speed_to_mps(speed, unit):
    if unit == "km/h":
        return speed / 3.6
    elif unit == "mph":
        return speed * 0.44704
    elif unit == "min/km":
        return 1000 / (speed * 60)

def convert_mps_to_speed(mps, unit):
    if unit == "km/h":
        return mps * 3.6
    elif unit == "mph":
        return mps / 0.44704
    elif unit == "min/km":
        return 1000 / (mps * 60)

# Velocidade
with tab1:
    st.subheader("Calcular Velocidade")
    col1, col2 = st.columns(2)
    with col1:
        distance = st.number_input("Distância", min_value=0.0, value=5.0)
        dist_unit = st.selectbox("Unidade de Distância", ["kilometers", "meters", "miles"])
    with col2:
        time_str = st.text_input("Tempo (hh:mm:ss)", value="00:25:00")
        speed_unit = st.selectbox("Unidade de Velocidade", ["km/h", "mph", "min/km"])

    time_sec = parse_time_input(time_str)

    if time_sec and time_sec > 0:
        distance_m = convert_distance_to_meters(distance, dist_unit)
        speed_mps = distance_m / time_sec
        result = convert_mps_to_speed(speed_mps, speed_unit)

        if speed_unit == "min/km":
            minutes = int(result)
            seconds = int((result - minutes) * 60)
            st.success(f"Velocidade: {minutes}:{seconds:02d} min/km")
        else:
            st.success(f"Velocidade: {result:.2f} {speed_unit}")
    elif time_str:
        st.error("Formato de tempo inválido. Use hh:mm:ss")

# Distância
with tab2:
    st.subheader("Calcular Distância")
    col1, col2 = st.columns(2)
    with col1:
        speed = st.number_input("Velocidade", min_value=0.0, value=10.0)
        speed_unit = st.selectbox("Unidade de Velocidade", ["km/h", "mph", "min/km"], key="dist_speed")
    with col2:
        time_str = st.text_input("Tempo (hh:mm:ss)", value="00:30:00", key="dist_time")
        dist_unit = st.selectbox("Unidade de Distância", ["kilometers", "meters", "miles"], key="dist_unit")

    time_sec = parse_time_input(time_str)

    if time_sec and time_sec > 0:
        if speed_unit == "min/km":
            pace_min = speed
            speed_mps = 1000 / (pace_min * 60)
        else:
            speed_mps = convert_speed_to_mps(speed, speed_unit)
        distance_m = speed_mps * time_sec
        distance_out = convert_meters_to_distance(distance_m, dist_unit)
        st.success(f"Distância: {distance_out:.2f} {dist_unit}")
    elif time_str:
        st.error("Formato de tempo inválido. Use hh:mm:ss")

# Tempo
with tab3:
    st.subheader("Calcular Tempo")
    col1, col2 = st.columns(2)
    with col1:
        distance = st.number_input("Distância", min_value=0.0, value=10.0, key="time_dist")
        dist_unit = st.selectbox("Unidade de Distância", ["kilometers", "meters", "miles"], key="time_unit")
    with col2:
        speed = st.number_input("Velocidade", min_value=0.0, value=12.0, key="time_speed")
        speed_unit = st.selectbox("Unidade de Velocidade", ["km/h", "mph", "min/km"], key="time_speed_unit")

    distance_m = convert_distance_to_meters(distance, dist_unit)
    if speed_unit == "min/km":
        speed_mps = 1000 / (speed * 60)
    else:
        speed_mps = convert_speed_to_mps(speed, speed_unit)

    if speed_mps > 0:
        time_sec = distance_m / speed_mps
        hours = int(time_sec // 3600)
        minutes = int((time_sec % 3600) // 60)
        seconds = int(time_sec % 60)
        st.success(f"Tempo: {hours:02d}:{minutes:02d}:{seconds:02d}")
    else:
        st.error("Velocidade inválida.")
