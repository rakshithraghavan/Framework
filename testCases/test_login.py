import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
#pytest -v -s testCases
#pytest -v -s testCases/test_login.py -m "sanity"
#pytest -v -s testCases/test_login.py -m "sanity" or "regression"
#pytest -v -s testCases/test_login.py -m "sanity" and "regression"
#pytest -v -s testCases/test_login.py --browser chrome
#pytest -v -s -n=2 testCases/test_login.py --browser chrome
#pytest -v -s testCases/test_login.py testCases/test_login_ddt.py --browser chrome
#pytest -v -s -n=2 --html=Reports/report.html testCases/test_login.py --browser chrome

class Test_001_Login:
    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()
    logger=LogGen.loggen()

    def test_homePageTitle(self,setup):
        self.logger.info("**********Test_001_Login**********")
        self.logger.info("**********Verifying Home Page Title**********")
        self.driver=setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        if act_title=="Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("**********Home Page Title Test Passed**********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.error("**********Home Page Title Test Failed**********")
            assert False

    def test_login(self, setup):
        self.logger.info("**********Verifying Login Test**********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title

        if act_title=="Dashboard / nopCommerce administration":
            assert True
            self.logger.info("**********Login Test Passed**********")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.error("**********Login Test Failed**********")
            assert False
