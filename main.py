import requests

city = input("請輸入城市名稱：")
api = "7f1a9376d21b282af01bda4bc8f83244"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}"

weather = requests.get(url)
temp = int(weather.json()["main"]["temp"] - 273.15)

print(f"{city} 目前的氣溫是 {temp} 度")