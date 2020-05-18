from selenium import webdriver
import pytest
import time
import math


@pytest.fixture(scope="function")
def browser():
    print("\nSTART")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nSTOP")
    time.sleep(2)
    browser.quit()

@pytest.mark.parametrize('link', ["236895", "236896", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])

class TestAllienPage():
    def test_allien_link1(self, browser, link): 
        link = f"https://stepik.org/lesson/{link}/step/1"
        browser.get(link)
        answer = str (math.log(int(time.time())))
        input1 = browser.find_element_by_css_selector("textarea.textarea")
        input1.send_keys(answer)
        button = browser.find_element_by_css_selector("button.submit-submission")
        button.click()
        x = browser.find_element_by_css_selector(".smart-hints__hint")
        #print (x.text)
        assert x.text == "Correct!", "Test failed"
      
        
        
       
        
        
        
        #x = browser.find_element_by_css_selector("pre.smart-hints__hint")
        
        #y = x.get_attribute("text")
        #print(y. text)
       # z = "Correct!"
        # assert y == z, "Test failed"
        #assert correct_txt == correct_txt1, "Test failed"
