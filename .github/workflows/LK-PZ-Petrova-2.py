from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

def search_wikipedia(query):
    browser = webdriver.Chrome()
    browser.get("https://ru.wikipedia.org/wiki/" + query)
    assert "Википедия" in browser.title
    time.sleep(5)

    return browser

def list_paragraphs(browser):
    paragraphs = browser.find_elements(By.TAG_NAME, "p")
    for paragraph in paragraphs:
        print(paragraph.text)
    input()

def navigate_to_related_page(browser):
    hatnotes = []
    for element in browser.find_elements(By.TAG_NAME, "div"):
        cl = element.get_attribute("class")
        if cl == "hatnote navigation-not-searchable":
            hatnotes.append(element)
    hatnote = random.choice(hatnotes)
    link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")
    browser.get(link)
    return browser

def main():
    query = input("Enter your search query: ")
    browser = search_wikipedia(query)

    while True:
        print("Choose an action:")
        print("1. List paragraphs")
        print("2. Navigate to a related page")
        print("3. Exit")
        action = input("Enter your choice: ")

        if action == "1":
            list_paragraphs(browser)
        elif action == "2":
            browser = navigate_to_related_page(browser)
        elif action == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
