from selenium.webdriver.common.by import By


class AmazonResultPage:
    SEARCH_INPUT = (By.ID, "twotabsearchtextbox")

    def __init__(self, browser):
        self.browser = browser

    def search_input_value(self):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        return search_input.get_attribute("value")

    def title(self):
        page_title = self.browser.title
        return page_title
