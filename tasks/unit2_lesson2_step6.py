from selenium import webdriver
import time 
import math
from idlelib import browser

def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))



link = "http://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    browser.execute_script("window.scrollBy(0, 100);")
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()
    option1 = browser.find_element_by_id("robotsRule")
    option1.click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:

    time.sleep(30)
 
    browser.quit()

