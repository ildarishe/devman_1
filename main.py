import requests


def make_request(city):
    url = f"https://wttr.in/{city}"
    payload = {"n": "", "T" : "", "q": "", "M": "", "lang": "ru"}
    try:
        response = requests.request(method="GET", url=url, params=payload)
        if response.status_code == 200:
            print(response.text)
        else:
            print("Упс... Что-то сломалось или в запросе есть ошибки")
    except:
        print("Сервер недоступен или в запросе есть ошибки")


if __name__ == '__main__':
    cities = ["Лондон", "Аэропорт Шереметьево", "Череповец"]
    for city in cities:
        make_request(city)