from selenium import webdriver
import pytest
#pip install webdriver-manager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# import time
driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser"#, action="store", default="chrome"
    )
#@pytest.fixture(scope="class")      ## decorator to create fixture and can be used on class level
@pytest.fixture()
def setup(request):     ## request is predefined object, which will be auto populated by pytest
    global driver
    browser=request.config.getoption("browser")   #pytest --browser "firefox"

     # parameter which can be passed with pytest command
    if browser == "chrome":
        driver = webdriver.Chrome("C:/Program Files/chromedriver.exe")
        print("Launching Chrome browser")
    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("Launching Firefox browser")
    elif browser == "IE":
        driver=webdriver.Ie()
        print("IE driver")
    else:
#        driver=webdriver.Edge()
        driver=webdriver.Edge(EdgeChromiumDriverManager().install())
    return driver

# @pytest.fixture()
# def setup():
#     driver=webdriver.Chrome("C:/Program Files/chromedriver.exe")
#     return driver



