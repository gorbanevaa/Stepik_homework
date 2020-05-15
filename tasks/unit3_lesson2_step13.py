from selenium import webdriver
import time
import unittest

class TestText(unittest.TestCase):
    def test_text1(self):
        link = "http://suninjuly.github.io/registration1.html"     
        browser = webdriver.Chrome()
        browser.get(link)
        # Код заполняющий поля ввода
        input1 = browser.find_element_by_css_selector(".first_block input.first")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector(".first_block input.second")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector(".first_block input.third")
        input3.send_keys("petrov@email.com")
        input4 = browser.find_element_by_css_selector(".second_block input.first")
        input4.send_keys("+79999999999")
        input5 = browser.find_element_by_css_selector(".second_block input.second")
        input5.send_keys("Russia , Moscow")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        # Проверяем что смогли зарегестрироваться
        # Ждем загрузки страницы
        time.sleep(1)
        # Находим элемент содеражщий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # Записываем в переменную welcom_text из элемента welcom_text_elt
        welcome_text = welcome_text_elt.text
        time.sleep(10)
        # Закрываем браузер после всех манипуляций
        browser.quit()
        # Проверяем с помощью "self.assertEqual" появилось сообщение об успешной регистрации 
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_text2(self):
        link = "http://suninjuly.github.io/registration2.html"     
        browser = webdriver.Chrome()
        browser.get(link)
        # Код заполняющий поля ввода
        input1 = browser.find_element_by_css_selector(".first_block input.first")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector(".first_block input.second")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector(".first_block input.third")
        input3.send_keys("petrov@email.com")
        input4 = browser.find_element_by_css_selector(".second_block input.first")
        input4.send_keys("+79999999999")
        input5 = browser.find_element_by_css_selector(".second_block input.second")
        input5.send_keys("Russia , Moscow")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        # Проверяем что смогли зарегестрироваться
        # Ждем загрузки страницы
        time.sleep(1)
        # Находим элемент содеражщий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # Записываем в переменную welcom_text из элемента welcom_text_elt
        welcome_text = welcome_text_elt.text
        time.sleep(10)
        # Закрываем браузер после всех манипуляций
        browser.quit()
        # Проверяем с помощью "self.assertEqual" появилось сообщение об успешной регистрации 
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        
if __name__ == "__main__":
    unittest.main()
