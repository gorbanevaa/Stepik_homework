from selenium import webdriver
import time 
import math
from idlelib import browser

def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))



link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    new_window = browser.window_handles[1]
    print(new_window)

finally:

    time.sleep(15)
 
    browser.quit()


