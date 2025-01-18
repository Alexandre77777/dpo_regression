import streamlit as st
import requests

st.title('Прогноз цени на жильё')

MedInc = st.slider("Медианный доход", 0, 1000, 8, 5)
HouseAge = st.slider("Средний возраст жилья", 0, 1000, 8, 5)
AveRooms = st.slider("Общее число комнат", 0, 1000, 8, 5)
AveBedrms = st.slider("Общее число спален", 0, 1000, 8, 5)
Population = st.slider("Население", 0, 1000, 8, 5)
AveOccup = st.slider("Среднее кол-во домохозяйств", 0, 1000, 8, 5)
Latitude = st.slider("Широта", 0, 1000, 8, 5)
Longitude = st.slider("Долгота", 0, 1000, 8, 5)

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
    url = 'http://127.0.0.1:8000/predict'
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