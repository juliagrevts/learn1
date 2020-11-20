weather = {'city': 'Москва', 'temperature': '20'}


weather['temperature'] = int(weather['temperature']) - 5
print(weather)

print(weather.get('country', 'Россия'))

