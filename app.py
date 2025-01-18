import streamlit as st
import requests

st.title('🏠 Прогноз цены на жильё в Калифорнии')

st.markdown("Введите параметры дома для получения прогноза цены:")

# Организуем поля ввода в колонки для компактности
col1, col2 = st.columns(2)

with col1:
    MedInc = st.number_input(
        "Медианный доход (в десятках тысяч $):",
        min_value=0.0, max_value=15.0, value=5.0, step=0.1
    )
    HouseAge = st.number_input(
        "Возраст дома (лет):",
        min_value=1, max_value=52, value=20, step=1
    )
    AveRooms = st.number_input(
        "Среднее количество комнат:",
        min_value=1.0, max_value=15.0, value=5.0, step=1.0
    )
    AveBedrms = st.number_input(
        "Среднее количество спален:",
        min_value=1.0, max_value=5.0, value=1.0, step=1.0
    )

with col2:
    Population = st.number_input(
        "Население района:",
        min_value=1, max_value=40000, value=1000, step=1
    )
    AveOccup = st.number_input(
        "Среднее количество жильцов:",
        min_value=1.0, max_value=1243.0, value=3.0, step=0.1
    )
    Latitude = st.number_input(
        "Широта:",
        min_value=32.0, max_value=42.0, value=36.0, step=0.01
    )
    Longitude = st.number_input(
        "Долгота:",
        min_value=-124.0, max_value=-114.0, value=-120.0, step=0.01
    )

if st.button("Получить прогноз"):
    data = {
        "MedInc": MedInc,
        "HouseAge": HouseAge,
        "AveRooms": AveRooms,
        "AveBedrms": AveBedrms,
        "Population": Population,
        "AveOccup": AveOccup,
        "Latitude": Latitude,
        "Longitude": Longitude
    }
    url = 'https://dpo-regression.onrender.com/predict'
    response = requests.post(url, json=data)

    if response.status_code == 200:
        try:
            data = response.json()
            prediction = data.get('prediction')
            if prediction is not None:
                st.success(f'💰 **Прогнозируемая цена: {prediction * 1000:.2f}$**')
            else:
                st.error("Ошибка: Ответ API не содержит прогноз.")
        except ValueError:
            st.error("Ошибка: Неверный формат ответа от API.")
    else:
        st.error(f"Ошибка: API вернул статус {response.status_code}.")