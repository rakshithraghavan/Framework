from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
search_box="//textarea[@id='APjFqb']"
search_box_id='//textarea[@class="gLFyf"]'
wiki_pedia="//h3[normalize-space()='Apple Inc.']"
driver=webdriver.Chrome("C:\drivers\chromedriver.exe")
driver.get("https://www.google.com/")
print(driver.title)
driver.find_element(By.CLASS_NAME, search_box_id).send_keys("apple")
print(driver.title)
driver.find_element(By.XPATH, search_box).send_keys(Keys.ENTER)
print(driver.title)
driver.find_element(By.XPATH,wiki_pedia).click()
print(driver.title)
print(driver.current_url)




