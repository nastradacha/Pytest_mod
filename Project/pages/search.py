from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json


class AmazonSearchPage:
    # import config file
    access_data = open(
        "C:\\Users\\Nastracha\\OneDrive\\Desktop\\Amazonian\\NasCode\\Project\\Config\\accessdata.json",
        "r",
    )
    access_data = json.load(access_data)
    URL = access_data["URL"]["AmazonMain"]

    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def search(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase + Keys.RETURN)