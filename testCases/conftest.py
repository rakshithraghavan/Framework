from selenium import webdriver
import pytest

@pytest.fixture()
def setup():
    driver=webdriver.Chrome("C:/Program Files/chromedriver.exe")
    return driver