import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID, "num1").text
    num2 = browser.find_element(By.ID, "num2").text
    x = int(num1) + int(num2)

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(x))

    option1 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    option1.click()

finally:
    time.sleep(10)
    browser.quit()
