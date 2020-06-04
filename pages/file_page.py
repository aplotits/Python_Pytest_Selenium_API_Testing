from .base_page import BasePage
from selenium.webdriver.common.by import By

class FilePage(BasePage):
    _file_to_upload = '/Users/alexplotitsa/Development/Rescale_Assignment/Data_File_One.txt'
    _file_list_container = '#file-list-container input'
    _progress_bar_span = '.progress-bar span'
    
    '''Upload file'''
    def upload_file(self):

        upload_file_element = self._driver.find_element(By.CSS_SELECTOR, self._file_list_container)
        upload_file_element.send_keys(self._file_to_upload)
        status_element = self._driver.find_element(By.CSS_SELECTOR, self._progress_bar_span)
        
        return status_element.text.strip()
