from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    link = browser.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
    link.click()

    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Andrey")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Negru")
    input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
    input3.send_keys("Saint-Petersburg")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(5)
browser.quit()

