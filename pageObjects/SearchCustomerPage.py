from selenium.webdriver.common.by import By


class SearchCustomer():
    # Add customer Page
    txtEmail_xpath = "//input[@id='SearchEmail']"
    txtFirstName_xpath="//input[@class='form-control text-box single-line' and @id='SearchFirstName']"
    txtLastName_xpath="//input[@class='form-control text-box single-line' and @id='SearchLastName']"
    btnSearch_xpath="//button[@id='search-customers']"
    tblSearchResults_xpath="(//table[@class='table table-bordered table-hover table-striped dataTable no-footer'])[2]"
    table_xpath="(//div[@class='col-md-12'])[1]"
    tableRows_xpath="(//table[@class='table table-bordered table-hover table-striped dataTable no-footer'])[2]//tbody/tr"
    tableColumns_xpath="(//table[@class='table table-bordered table-hover table-striped dataTable no-footer'])[2]//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.txtEmail_xpath).clear()
        self.driver.find_element(By.XPATH,self.txtEmail_xpath).send_keys(email)

    def setFirstName(self,fname):
        self.driver.find_element(By.XPATH,self.txtFirstName_xpath).clear()
        self.driver.find_element(By.XPATH,self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element(By.XPATH,self.txtLastName_xpath).clear()
        self.driver.find_element(By.XPATH,self.txtLastName_xpath).send_keys(lname)

    def clickSearch(self):
        self.driver.find_element(By.XPATH,self.btnSearch_xpath).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH, self.tableRows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements(By.XPATH,self.tableColumns_xpath))

    def searchCustomerByEmail(self,email):
        flag=False
        for r in range(1,self.getNoOfRows()+1):
          table=self.driver.find_element(By.XPATH,self.table_xpath)
          emailid=table.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
          if emailid == email:
              flag = True
              break
        return flag

    def searchCustomerByName(self,Name):
        flag=False
        for r in range(1,self.getNoOfRows()+1):
          table=self.driver.find_element(By.XPATH,self.table_xpath)
          name=table.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text
          if name == Name:
              flag = True
              break
        return flag


