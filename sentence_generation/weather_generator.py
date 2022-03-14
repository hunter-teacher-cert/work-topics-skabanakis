import random
weather_chain = {
    'sun': ['sun', 'sun', 'sun', 'sun', 'sun', 'sun', 'sun', 'sun', 'sun', 'rain'],
    'rain': ['sun', 'rain','snow'],
    'snow':['sun', 'rain', 'snow','cloudy'],
    'cloudy':['sun','rain','snow','cloudy','sun']
}

weather = [random.choice(list(weather_chain.keys()))]

for i in range(10):
    weather.append(random.choice(weather_chain[weather[i]]))

print(weather)