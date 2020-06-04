from .base_page import BasePage
from .home_page import HomePage
from selenium.webdriver.common.by import By

class SigninPage(BasePage):
    _input_email_address = 'alex.plotitsa@gmail.com'
    _active_input = '.active-input'
    _password = 'password'
    _delayed_start = '.delayed-start .input-link'
    _path = 'path'


    '''Sign into application'''
    def signin(self):
        self._element_email_address = self._driver.find_element(By.CSS_SELECTOR, self._active_input)
        self._element_email_address.send_keys(self._input_email_address)
        self._driver.find_element(By.CSS_SELECTOR, self._path).click()
        self._driver.find_element(By.NAME, self._password).send_keys("RescaleKama$utra")
        self._driver.find_element(By.CSS_SELECTOR, self._delayed_start).click()

        return HomePage(self._driver)

