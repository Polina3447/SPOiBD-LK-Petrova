import requests

# URL API GitHub для поиска репозиториев
url = "https://api.github.com/search/repositories"

# Параметры запроса
params = {
    "q": "html in:readme"  # Поиск репозиториев, в которых упоминается HTML в README
}

# Отправка GET-запроса
response = requests.get(url, params=params)

# Печать статус-кода ответа
print("Статус-код:", response.status_code)

# Печать содержимого ответа в формате JSON
if response.status_code == 200:
    print("Содержимое ответа (JSON):")
    print(response.json())
else:
    print("Ошибка при выполнении запроса:", response.text)
