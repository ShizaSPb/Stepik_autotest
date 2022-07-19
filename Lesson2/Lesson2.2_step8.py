from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Andrey")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Negru")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("Shiza1388@gmail.com")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'Test.txt')
    input4 = browser.find_element(By.ID, "file")
    input4.send_keys(file_path)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    time.sleep(5)
browser.quit()

