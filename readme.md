# Тестовое задание - API продажа машин автодилерами

## RESTful Структура

### Эндпоинты для работы дилера с машинами

|           |          GET        |       POST      |      PUT       |       DELETE       |
| --------- | ------------------- | --------------- | -------------- | ------------------ |
| /cars/    | Показать все записи | Добавить запись |      N/A       | Удалить все записи |
| /cars/id/ |   Показать по id    |       N/A       | Изменить по id |   Удалить по id    |

### Эндпоинты для регистрации и получение токена

|                    |        POST         |
| ------------------ | ------------------- |
| /account/register/ |     Регистрация     |
|  /api-token-auth/  |  Получение токена   |

## Настройка

### 1. python manage.py makemigrations

### 2. python manage.py migrate

### 3. (Опционально) python manage.py createsuperuser

### 4. Создание пользователя(дилера) осуществляется с помощью POST запроса на /account/register/ включающего в себя payload
```json
{"username": "username",
"password": "password"}
```
### 5. Получение токена для возможности использования API осуществляется включающего в себя payload с помощью запроса POST запроса на /api-token-auth/  включающего в себя payload
```json
{"username": "username",
"password": "password"}
```
## Использование API

Чтобы использовать эндпоинты для работы с машинами, требуется добавить в Headers ключ
```json
{
  "Authorization": "Token ваш_токен_полученный_на_5_этапе"
}
```

## Примеры

###Получить все записи
```python
import requests

url = "http://127.0.0.1:8000/cars/"

payload={}
headers = {
  'Authorization': 'Token ваш_токен'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

```

### Получить конкретную запись
```python
import requests

url = "http://127.0.0.1:8000/cars/id_записи/"

payload={}
headers = {
  'Authorization': 'Token ваш_токен'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

```

### Добавить запись
```python
import requests
import json

url = "http://127.0.0.1:8000/cars/"

payload = json.dumps({
  "car_model": {
    "brand": "Chevrolet",
    "model": "Camaro ZL1",
    "gen": "6"
  },
  "equipment": [
    {
      "body": "Coupe",
      "transmission": "Auto",
      "engine": "LT4 V8",
      "color": "Yellow"
    }
  ],
  "price": {
    "car_price": 55500
  },
  "mileage": [
    {
      "car_mileage": 1200
    }
  ],
  "quantity": {
    "car_quantity": 70
  }
})
headers = {
  'Authorization': 'Token ваш_токен',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

```

### Изменить конкретную запись
```python
import requests
import json

url = "http://127.0.0.1:8000/cars/id_записи/"

payload = json.dumps({
  "car_model": {
    "brand": "Chevrolet",
    "model": "Camaro ZL1",
    "gen": "5"
  },
  "equipment": [
    {
      "body": "Coupe",
      "transmission": "Auto",
      "engine": "LT4 V8",
      "color": "White"
    }
  ],
  "price": {
    "car_price": 35000
  },
  "mileage": [
    {
      "car_mileage": 200
    }
  ],
  "quantity": {
    "car_quantity": 20
  }
})
headers = {
  'Authorization': 'Token ваш_токен',
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)

```

### Удалить запись
```python
import requests

url = "http://127.0.0.1:8000/cars/id_записи/"

payload={}
headers = {
  'Authorization': 'Token ваш_токен'
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)

```
### Все примеры использования API приведены в тестах [tests.py](tests.py)

### Выполните python manage.py tests для запуска тестов