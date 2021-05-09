import json

test_json = json.dumps({
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

test_json_put = json.dumps({
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
        "car_price": 30000
    },
    "mileage": [
        {
            "car_mileage": 1000
        }
    ],
    "quantity": {
        "car_quantity": 20
    }
})
