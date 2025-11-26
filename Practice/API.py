import requests


def easy_task(name: str):
    city = name
    API_key = ""
    response = requests.get(f"http://api.weatherapi.com/v1/current.json?key={API_key}&q={city}&aqi=no")
    data = response.json()
    print(f"{data["current"]["temp_c"]}°C")


def medium_task(amount: int, source: str, target: str):
    key = ""
    link = f"https://v6.exchangerate-api.com/v6/{key}/latest/{source}"
    response = requests.get(link)
    data = response.json()
    return amount * data["conversion_rates"][target]


def hard_task(keyword: str):
    key = ""
    url = f"https://www.googleapis.com/books/v1/volumes?q={keyword}&key={key}"

    response = requests.get(url)
    data = response.json()


    for i in data["items"][:5]:
        info = i["volumeInfo"]
        print(f"{info["title"]} written by {info["authors"]} and published on the {info["publishedDate"]}")



# easy_task("London")
# print(medium_task(40000, "HUF", "EUR"))
# hard_task("python")

