import json

file = open('friends_json.txt', 'r')
# converts to a dictionary
file_contents = json.load(file)

file.close()

print(file_contents["friends"][0])

cars = [
    {'make': 'Ford', 'model': 'Fiesta'},
    {'make': 'Ford', 'model': 'Focus'},
    {'make': 'Ford', 'model': 'Explorer'}
]

file = open('cars_json.txt', 'w')
json.dump(cars, file)
file.close()

my_json_string = '[{"name": "Alfa Romeo", "released": 1950}]'

incorrect_car = json.loads(my_json_string)
print(incorrect_car[0]['name'])