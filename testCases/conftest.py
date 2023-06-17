#https://console-nz-dev-eks-cluster9.us-east-2.data-warehouse.test.cloud.ibm.com/#/?crn=crn:v1:staging:public:data-warehouse:us-east:a/957e778044cc43a2ae9195d58a500b7f:ff853eb6-1fc2-449f-875a-67dd4b81dd96::
from selenium import webdriver
import pytest
#pip install webdriver-manager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# import time
driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome"
    )
#@pytest.fixture(scope="class")      ## decorator to create fixture and can be used on class level
@pytest.fixture()
def setup(request):     ## request is predefined object, which will be auto populated by pytest
    global driver
    browser=request.config.getoption("browser")   #pytest --browser "firefox"

     # parameter which can be passed with pytest command
    if browser == "chrome":
        driver = webdriver.Chrome("C:\drivers\chromedriver.exe")
        #driver = webdriver.Chrome()
        print("Launching Chrome browser")
    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("Launching Firefox browser")
    elif browser == "Edge":
#        driver=webdriver.Edge()
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        print("Edge driver")
    else:
        driver=webdriver.Chrome()
    return driver

# @pytest.fixture()
# def setup():
#     driver=webdriver.Chrome("C:/Program Files/chromedriver.exe")
#     return driver


#Pytest HTML report
#Hook for adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Framework'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Rakshith'

#Hook for delete/modify Environment info to HTML Report
#@pytest.mark.optionalhook
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)


