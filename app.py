import streamlit as st
import requests

st.title('Прогноз цени на жильё')

MedInc = st.slider("Медианный доход", 0, 1000, 8, 1)
HouseAge = st.slider("Средний возраст жилья", 0, 200, 8, 1)
AveRooms = st.slider("Общее число комнат", 0, 15, 8, 1)
AveBedrms = st.slider("Общее число спален", 0, 5, 8, 1)
Population = st.slider("Население", 0, 1000, 8, 1)
AveOccup = st.slider("Среднее кол-во домохозяйств", 0, 1000, 8, 1)
Latitude = st.slider("Широта", -180, 180, 8, 1)
Longitude = st.slider("Долгота", -180, 180, 8, 1)

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
                st.success(f'Прогнозируемая цена: {prediction*1000:.2f}$')
            else:
                st.error("Ошибка: Ответ API не содержит прогноз.")
        except ValueError:
            st.error("Ошибка: Ответ API не является валидным прогнозом.")
    else:
        st.error(f"Ошибка: Ответ API вернул статус {response.status_code}.")