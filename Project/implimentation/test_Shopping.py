import json
from selenium import webdriver
import pytest
from pages.search import AmazonSearchPage
from pages.result import AmazonResultPage

# import config file
@pytest.fixture(scope="session")
def config():
    with open(
        "C:\\Users\\Nastracha\\OneDrive\\Desktop\\Amazonian\\NasCode\\Project\\Config\\accessdata.json"
    ) as config_file:
        access_data = json.load(config_file)
        return access_data

C:/Users/Nastracha/OneDrive/Desktop/Amazonian/NasCode/Project/implimentation
# access_data = open(
#     "C:\\Users\\Nastracha\\OneDrive\\Desktop\\Amazonian\\NasCode\\Project\\Config\\accessdata.json",
#     "r",
# )
# access_data = json.load(access_data)
#
# print(access_data)


# def open_browser(browser_driver):  # Function to open browser, Add driver path
@pytest.fixture
def browser(config):
    if 'Chrome_driver' in config['Browsers']:
        driver = webdriver.Chrome(config["Browsers"]["Chrome_driver"])
    elif 'Firefox_driver' in config['Browsers']:
        driver = webdriver.Firefox(executable_path=(config["Browsers"]["Firefox_driver"]))
    else:
        raise Exception(f'"{config["Browsers"]}" is not a supported browser')
    # driver = Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_amazon_search(browser):
    phrase = "s197 v6"

    search_page = AmazonSearchPage(browser)
    search_page.load()
    search_page.search(phrase)

    result_page = AmazonResultPage(browser)
    assert "Amazon.com:" in result_page.title()
    assert result_page.search_input_value() == phrase

    browser.quit()


if __name__ == "__main__":
    pytest.main()
