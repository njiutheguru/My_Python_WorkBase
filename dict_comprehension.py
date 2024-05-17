sentence = "What is the airspeed velocity of an unaladen swallow?"

dict = {key: len(key) for key in sentence.split()}

print(dict)

weather_c = {
    "Monday": 23,
    "Tuesday": 43, 
    "Wednesday": 33, 
    "Thursday": 21,
    "Friday": 25,
    "Saturday": 32,
    "Sunday": 17
}
f_weather = {key: (value * 9/5 )+ 32 for (key, value) in weather_c.items()}

print(f_weather)