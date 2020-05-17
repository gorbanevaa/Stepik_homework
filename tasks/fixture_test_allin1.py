import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="class")
def browser():
    print("^_^", "\n")
    browser = webdriver.Chrome()
    yield browser
    print(":3", "\n")
    browser.quit()

@pytest.fixture()
def browser1():
    print(":)", "\n")    

@pytest.fixture(autouse=True)
def prepare_data():
    print(":-Р", "\n")


class TestMainPage1():
    def test_guest_should_see_login_link(self, browser, browser1):
        # не передаём как параметр фикстуру prepare_data, но она все равно выполняется
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")