import requests


def get_forecast(city):
    url = f"https://wttr.in/{city}"
    payload = {"n": "", "T" : "", "q": "", "M": "", "lang": "ru"}
    response = requests.request(method="GET", url=url, params=payload)
    if response.ok:
        return response.text
    else:
        return "Упс... Что-то сломалось или в запросе есть ошибки"




if __name__ == '__main__':
    cities = ["Лондон", "Аэропорт Шереметьево", "Череповец"]
    for city in cities:
        try:
            print(get_forecast(city))
        except:
            print("Сервер недоступен или в запросе есть ошибки")
