import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
import requests
import os
import json
from  ..pages.signin_page import SigninPage
from .constants import *



@pytest.fixture(scope="class")
def driver_init(request):
    ff_driver = webdriver.Firefox(executable_path=GECKO_DRIVER_PATH)
    ff_driver.implicitly_wait(30)
    ff_driver.maximize_window()
    request.cls.driver = ff_driver
    yield
    ff_driver.close()


@pytest.mark.usefixtures("driver_init")
class BasicTest:
    pass


class TestRescale(BasicTest):
    def test_upload_file(self):
        self.driver.get(BASE_URL)
        signin_page = SigninPage(self.driver)
        home_page = signin_page.signin()
        file_page = home_page.click_file_tab()
        status = file_page.upload_file()

        assert status == '100%'


class TestAPI():
    def test_api_upload_file(self):
        # url = "https://platform.rescale.com/api/v2/files/contents/"
        url = API_URL
        authoriazation_token = AUTHORIZATION_TOKEN
        headers = {'Authorization' : authoriazation_token}
        file_path = FILE_PATH
        files = {'file': open(file_path, 'rb')}
        response = requests.post(url, files=files, headers=headers)
        assert response.status_code == 201
        json_response = json.loads(response.text)
        assert json_response['isUploaded'] == True


        
