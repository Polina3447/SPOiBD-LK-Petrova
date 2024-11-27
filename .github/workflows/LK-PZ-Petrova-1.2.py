import requests

# URL API JsonPlaceholder
url = "https://jsonplaceholder.typicode.com/posts"

# Параметры запроса
params = {
    "userId": 1  # Фильтрация по userId = 1
}

# Отправка GET-запроса
response = requests.get(url, params=params)

# Печать полученных записей
if response.status_code == 200:
    posts = response.json()
    for post in posts:
        print("Post ID:", post["id"])
        print("Title:", post["title"])
        print("Body:", post["body"])
        print("---")
else:
    print("Ошибка при выполнении запроса:", response.text)
