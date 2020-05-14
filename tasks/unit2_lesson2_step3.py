from selenium import webdriver
import time 
import math
from idlelib import browser



link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    num1 = browser.find_element_by_id("num1")
    x = num1.text         
    num2 = browser.find_element_by_id("num2")
    y = num2.text
    z = str(int(x) + int(y))
    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(z) 
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:

    time.sleep(15)
 
    browser.quit()

