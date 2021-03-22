import json

with open('friends_json.txt', 'r') as file:
    # converts to a dictionary
    file_contents = json.load(file)


print(file_contents["friends"][0])

cars = [
    {'make': 'Ford', 'model': 'Fiesta'},
    {'make': 'Ford', 'model': 'Focus'},
    {'make': 'Ford', 'model': 'Explorer'}
]

with open('cars_json.txt', 'w') as file:
    json.dump(cars, file)


my_json_string = '[{"name": "Alfa Romeo", "released": 1950}]'

incorrect_car = json.loads(my_json_string)
print(incorrect_car[0]['name'])
