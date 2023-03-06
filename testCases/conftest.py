from selenium import webdriver
import pytest

# import time
# driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )
@pytest.fixture(scope="class")      ## decorator to create fixture and can be used on class level
def setup(request):     ## request is predefined object, which will be auto populated by pytest
    global driver
    browser_name=request.config.getoption("browser_name")   #pytest --browser_name "firefox"

     # parameter which can be passed with pytest command
    if browser_name == "chrome":
        driver = webdriver.Chrome("C:/Program Files/chromedriver.exe")
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "IE":
        print("IE driver")
    else:
        driver = webdriver.Chrome()


@pytest.fixture()
def setup():
    driver=webdriver.Chrome("C:/Program Files/chromedriver.exe")
    return driver
