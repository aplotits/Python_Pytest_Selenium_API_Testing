from .base_page import BasePage
from .file_page import FilePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
   _menu_files_dn = '#menuFiles .dn'
   
   def click_file_tab(self):
       self._driver.find_element(By.CSS_SELECTOR, self._menu_files_dn).click()
       return FilePage(self._driver)