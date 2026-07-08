import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import allure
import pytest


class TestHootel(object):
    def setup_method(self):
        URL = 'http://hotel-v3.progmasters.hu/'
        options = Options()
        # options.add_argument("start-maximized")
        options.add_argument("--headless")
        options.add_experimental_option("detach", True)
        self.browser = webdriver.Chrome(options=options)
        self.browser.get(URL)
        print(self.browser.get_window_size()) #{'width': 780, 'height': 580}
        self.browser.maximize_window()
        print(self.browser.get_window_size()) # {'width': 800, 'height': 600}
        self.browser.set_window_size(1024,700)
        print(self.browser.get_window_size())

    def teardown_method(self):
        self.browser.quit()

    @allure.title("Hootel Login")
    @allure.description("A belépés tesztelése")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("login", "hotel", "selenium")
    def test_login(self):
        email = 'hiwasi1765@wisnick.com'
        password = 'tesztelek2021'

        login_btn = self.browser.find_element(By.XPATH, '//a[@class="nav-link"]')
        login_btn.click()

        email_input = self.browser.find_element(By.ID, 'email')
        email_input.send_keys(email)

        password_input = self.browser.find_element(By.ID, 'password')
        password_input.send_keys(password)

        submit_btn = self.browser.find_element(By.NAME, 'submit')
        submit_btn.click()
        time.sleep(1)

        logout_btn = self.browser.find_element(By.ID, 'logout-link')

        allure.dynamic.description(f"email: {email}, password = {password}")

        assert logout_btn.text == "Kilépés"

    @allure.title("Hootel List")
    @allure.description("Hotelek lista teszt")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("list", "hotel", "selenium")
    def test_hotel_list(self):
        hotel_list_btn = self.browser.find_element(By.XPATH, '//button[@class="btn btn-outline-primary btn-block"]')
        hotel_list_btn.click()
        time.sleep(1)

        hotel_list = self.browser.find_elements(By.XPATH, '//h4[@style="cursor: pointer"]')
        assert len(hotel_list) != 0
        assert len(hotel_list) == 10
