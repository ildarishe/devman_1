import requests

cities = ["Лондон", "Шереметьево", "Череповец"]
for city in cities:
    url = f"https://wttr.in/{city}?nTqM&lang=ru"
    response = requests.request(method="GET", url=url)
    print(response.text)