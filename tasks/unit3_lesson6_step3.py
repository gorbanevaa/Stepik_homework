from selenium import webdriver
import pytest
import time
import math

def calc(x):
      return str (math.log(int(time.time())))

@pytest.fixture(scope="class")
def browser():
    print("\nSTART")
    browser = webdriver.Chrome()
    yield browser
    print("\nSTOP")
    time.sleep(10)
    browser.quit()

class TestAllienPage():
    def test_allien_link1(self, browser):
        browser.get("https://stepik.org/lesson/236895/step/1")
        time.sleep(10)
        x = calc
        input1 = browser.find_element_by_id("ember68")
        input1.send_keys(calc(x))
        button = browser.find_element_by_class("submit-submission")
        button.click()