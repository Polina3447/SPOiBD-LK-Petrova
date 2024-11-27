
from selenium import webdriver
import time

browser = webdriver.Chrome()

browser.get("https://en.wikipedia.org/wiki/Document_Object_Model")
time.sleep(10)
#Задержка в 10 секунд
# browser.quit()
#Закрываем браузер


browser.get("https://en.wikipedia.org/wiki/Document_Object_Model")
time.sleep(10)
browser.get("https://ru.wikipedia.org/wiki/Selenium")

browser.get("https://en.wikipedia.org/wiki/Document_Object_Model")
browser.save_screenshot("Object_Model.png")
#В кавычках указываем название, которое присвоится скриншоту
time.sleep(10)
browser.get("https://ru.wikipedia.org/wiki/Selenium")
browser.save_screenshot("selenium.png")

browser.get("https://en.wikipedia.org/wiki/Document_Object_Model")
browser.save_screenshot("dom.png")
time.sleep(5)
browser.get("https://ru.wikipedia.org/wiki/Selenium")
browser.save_screenshot("selenium.png")
time.sleep(3)
browser.refresh()

#Открыло страницу через браузер

from selenium import webdriver
from selenium.webdriver import Keys
#Библиотека, которая позволяет вводить данные на сайт с клавиатуры
from selenium.webdriver.common.by import By
#Библиотека с поиском элементов на сайте
import time

browser = webdriver.Chrome()
browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")
assert "Википедия" in browser.title
time.sleep(5)

search_box = browser.find.element(By.ID, "searchInput")
search_box.send_keys("Солнечная система")
search_box.send_keys(Keys.RETURN)
time.sleep(5)

a = browser.find_element(By.LINK_TEXT, "Солнечная система")
#Добавляем клик на элемент
#find_element находит первый попавшийся элемент, подходящий под условия поиска.
#find_elements находит несколько элементов.


from selenium import webdriver
from selenium.webdriver import Keys
#Библиотека, которая позволяет вводить данные на сайт с клавиатуры
from selenium.webdriver.common.by import By
#Библиотека с поиском элементов на сайте
import time
import random

browser = webdriver.Chrome()

browser.get("https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D0%BB%D0%BD%D0%B5%D1%87%D0%BD%D0%B0%D1%8F_%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0")
paragraphs = browser.find_elements(By.TAG_NAME, "p")

'''
#Для перебора пишем цикл
for paragraph in paragraphs:
print(paragraph.text)
input()
'''

hatnotes = []
for element in browser.find_elements(By.TAG_NAME, "div"):
#Чтобы искать атрибут класса
    cl = element.get.attribute("class")
    if cl == "hatnote navigation-not-searchable":
        hatnotes.append(element)


print(hatnotes)
hatnote = random.choice(hatnotes)
#Для получения ссылки мы должны найти на сайте тег "a" внутри тега "div"
link = hatnote.find_element(By.TAG_NAME, "a").get.attribute("href")
browser.get(link)
