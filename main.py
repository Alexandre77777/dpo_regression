from fastapi import FastAPI  # Импортируем класс FastAPI из модуля fastapi для создания веб-приложения
import pickle  # Импортируем модуль pickle для загрузки сохраненных моделей
import numpy as np  # Импортируем библиотеку numpy для работы с массивами чисел
from pydantic import BaseModel  # Импортируем BaseModel из pydantic для валидации входных данных

app = FastAPI()  # Создаем экземпляр приложения FastAPI

class InputData(BaseModel):
    # Определяем модель входных данных с указанием типов данных для валидации
    MedInc: float       # Медианный доход
    HouseAge: float     # Средний возраст домов
    AveRooms: float     # Среднее количество комнат
    AveBedrms: float    # Среднее количество спален
    Population: float   # Население
    AveOccup: float     # Среднее количество жильцов на дом
    Latitude: float     # Широта
    Longitude: float    # Долгота

# Открываем файл с сохраненными объектами (моделью и обработчиком признаков)
with open('best_regression_model.pkl', 'rb') as f:
    saved_objects = pickle.load(f)  # Загружаем объекты из файла с помощью pickle

feature_engineering = saved_objects["pipeline"]  # Извлекаем конвейер обработки признаков
best_model = saved_objects["model"]              # Извлекаем обученную модель

@app.post('/predict')  # Создаем маршрут для POST-запроса по адресу '/predict'
async def predict(input_data: InputData):
    # Определяем асинхронную функцию обработки запроса с входными данными типа InputData

    # Формируем массив с данными из входного объекта
    X_new = np.array([[
        input_data.MedInc,
        input_data.HouseAge,
        input_data.AveRooms,
        input_data.AveBedrms,
        input_data.Population,
        input_data.AveOccup,
        input_data.Latitude,
        input_data.Longitude
    ]])

    # Применяем обработку признаков к новым данным
    X_new_transformed = feature_engineering.transform(X_new)

    # Получаем предсказание модели на основе обработанных данных
    prediction = best_model.predict(X_new_transformed)

    # Возвращаем результат предсказания в формате JSON
    return {'prediction': float(prediction[0])}