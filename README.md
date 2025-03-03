# 🏠 Прогнозирование стоимости жилья в Калифорнии

## 📝 Описание проекта

Это веб-приложение позволяет пользователям предсказывать цену жилья на основе различных параметров недвижимости. 📈💡

**Пользователи могут:**

- 📋 Вводить характеристики объекта недвижимости, такие как медианный доход в районе, возраст дома, среднее количество комнат и спален, население района и другие.
- 🖥️ Получать прогнозируемую стоимость жилья с помощью предварительно обученной регрессионной модели.

**Ссылка на развернутое приложение: https://dpo-regression.streamlit.app/**

## 📁 Структура проекта

- **`app.py`**  
  Фронтенд-приложение на **Streamlit**:
  - 🖥️ Отображает веб-интерфейс для ввода пользователем параметров недвижимости.
  - 🌐 Отправляет запросы к API для получения предсказаний стоимости.
  - 📊 Отображает результат предсказания на странице.

- **`main.py`**  
  Бэкенд-приложение на **FastAPI**:
  - 🚪 Определяет API-эндпоинт `/predict`, который принимает входные данные в формате JSON.
  - 📂 Загружает сохранённую модель регрессии из файла `best_regression_model.pkl`.
  - 🧮 Выполняет предобработку входных данных и возвращает предсказание стоимости.

- **`best_regression_model.pkl`**  
  🎓 Сериализованная (pickle) регрессионная модель машинного обучения, обученная на данных о ценах на жильё в Калифорнии.

- **`requirements.txt`**  
  📜 Файл со списком необходимых библиотек и зависимостей для запуска приложения.

## 🚀 Используемые технологии

- **Python** 🐍: язык программирования для разработки приложения.
- **Streamlit** 🌐: фреймворк для создания интерактивных веб-приложений на Python.
- **FastAPI** ⚡: современный высокопроизводительный фреймворк для создания API.
- **scikit-learn** 📚: библиотека машинного обучения для обучения и сохранения модели.
- **NumPy** 🔢: библиотека для научных вычислений и работы с массивами.
- **Pickle** 🥒: модуль для сериализации и десериализации объектов Python.
- **Requests** 📡: библиотека для отправки HTTP-запросов.

## 🛠️ Установка и запуск

Следуйте инструкциям ниже для установки и запуска приложения на локальном компьютере.

### 1. 🐙 Клонирование репозитория

```bash
git clone https://github.com/Alexandre77777/dpo_regression.git
cd dpo_regression
```

### 2. 🌳 Создание и активация виртуального окружения

**На Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**На macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. 📦 Установка зависимостей

```bash
pip install -r requirements.txt
```

### 4. 🚀 Запуск бэкенд-сервера (FastAPI)

В отдельном терминале запустите команду:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

### 5. 🌐 Запуск фронтенд-приложения (Streamlit)

В другом терминале выполните:

```bash
streamlit run app.py
```

### 6. 🌍 Открытие приложения в браузере

Перейдите по адресу [http://localhost:8501](http://localhost:8501) в вашем веб-браузере, чтобы открыть веб-интерфейс приложения.

## 🎮 Использование приложения

1. **Ввод параметров недвижимости:**

   Введите следующие параметры в соответствующие поля:

   - **MedInc** 💰: Медианный доход в районе (в десятках тысяч долларов).
   - **HouseAge** 🏚️: Возраст дома (в годах).
   - **AveRooms** 🛏️: Среднее количество комнат на домохозяйство.
   - **AveBedrms** 💤: Среднее количество спален на домохозяйство.
   - **Population** 👥: Количество людей, проживающих в районе.
   - **AveOccup** 🏘️: Среднее количество жильцов на домохозяйство.
   - **Latitude** 🗺️: Географическая широта района.
   - **Longitude** 🧭: Географическая долгота района.

2. **Получение предсказания:**

   Нажмите кнопку **"💡 Предсказать стоимость"**, чтобы отправить данные на сервер и получить прогнозируемую стоимость жилья.

3. **Просмотр результата:**

   Приложение отобразит предсказанную стоимость жилья в долларовом эквиваленте. 💲🏠

## 📝 Примечания

- 🔄 Убедитесь, что бэкенд-сервер на FastAPI запущен и доступен по адресу `http://localhost:8000`.
- ⚙️ Если вы изменили порт или хост при запуске сервера, обновите соответствующие настройки в файле `app.py`.
- 🌍 Модель использует данные о жилье в Калифорнии, поэтому точность предсказаний наиболее релевантна для этого региона.

## 📄 Лицензия

Данный проект распространяется под лицензией **MIT**. Более подробную информацию смотрите в файле [LICENSE](https://mit-license.org/license.txt).
