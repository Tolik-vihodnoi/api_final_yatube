# Проект «API для Yatube»

Описание проекта:


## Технологии

- Python
- Django
- Django REST Framework
- Djoser
- Redoc


## Установка

1. Склонируйте репозиторий и зайдите в директорию:

   git clone https://github.com/Tolik-vihodnoi/api_final_yatube.git &&
   cd api_final_yatube

2. Создайте виртуальную среду и активируйте ее:

   python -m venv venv
   source venv/bin/activate

3. Установите зависимости:

   pip intstall -U pip &&
   pip install -r requirements.txt

4. Примените миграции:

   python manage.py migrate

5. Запустите сервер:

   python manage.py runserver

6. Откройте приложение в браузере по адресу http://localhost:8000/


## Пример API запроса

1. Получение токена

Отправить POST запрос на эндпоинт api/v1/jwt/create/.

Payload:
{
  "username": "__ваше_имя__",
  "password": "__ваш_пароль__"
}

Response:
{
  "refresh": "string",
  "access": "string"
}


# Документаия API проекта

**http://127.0.0.1:8000/redoc/**
