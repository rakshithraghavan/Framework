# import time
#
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select

import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class AddCustomer:
    # Add customer Page
    lnkCustomers_menu_css = "body > div:nth-child(3) > aside:nth-child(2) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > nav:nth-child(2) > ul:nth-child(1) > li:nth-child(4) > a:nth-child(1) > p:nth-child(2)"
    #lnkCustomers_menu_xpath = "//body/div[@class='wrapper']/aside[@class='main-sidebar sidebar-dark-primary elevation-4 sidebar-focused']/div[@class='sidebar os-host os-theme-light os-host-resize-disabled os-host-transition os-host-scrollbar-horizontal-hidden os-host-overflow os-host-overflow-y']/div[@class='os-padding']/div[@class='os-viewport os-viewport-native-scrollbars-invisible']/div[@class='os-content']/nav[@class='mt-2']/ul[@role='menu']/li[1]/a[1]"
    #lnkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    #lnkCustomers_menu_xpath = "//a[@href='#']//span[contains(text(),'Customers')]"
    #lnkCustomers_menu_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    #lnkCustomers_menu_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a/p"
    #lnkCustomers_menuitem_xpath = "//span[@class='menu-item-title'][contains(text(),'Customers')]"
    #lnkCustomers_menuitem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    #lnkCustomers_menuitem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    lnkCustomers_menuitem_css = "body > div:nth-child(3) > aside:nth-child(2) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > nav:nth-child(2) > ul:nth-child(1) > li:nth-child(4) > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1) > p:nth-child(2)"
    #btnAddnew_xpath = "//a[@class='btn bg-blue']"
    #btnAddnew_xpath = "//a[@class='btn btn-primary']"
    btnAddnew_css = ".fas.fa-plus-square"
    #btnAddnew_xpath = "//a[@class='btn btn-primary']"
    customerInfo_css=".card-header.with-border.clearfix"
    #txtEmail_xpath = "//input[@id='Email']"
    txtEmail_css = "#Email"
    #txtPassword_xpath = "//input[@id='Password']"
    txtPassword_css = "#Password"
    txtcustomerRoles_css = "div[class='k-widget k-multiselect k-multiselect-clearable k-state-hover k-state-focused k-state-border-down'] div[role='listbox']"
    txtcustomerRoles_xpath = "(//div[@role='listbox'])[2]"
    #txtcustomerRoles_xpath = "//div[@class='k-widget k-multiselect k-multiselect-clearable k-state-hover k-state-focused k-state-border-down']//div[@role='listbox']"
    txtcustomerRoles_css= "div[class='k-widget k-multiselect k-multiselect-clearable k-state-hover k-state-focused k-state-border-down'] div[role='listbox']"
    #lstitemAdministrators_xpath = "//li[contains(text(),'Administrators')]"
    lstitemAdministrators_xpath = "//li[contains(text(),'Administrators')]"
    lstitemAdministrators_css = "body > div:nth-child(3) > div:nth-child(3) > form:nth-child(2) > section:nth-child(4) > div:nth-child(1) > div:nth-child(1) > nop-cards:nth-child(1) > nop-card:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(10) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(1) > span:nth-child(1)"
    #lstitemRegistered_xpath = "//li[contains(text(),'Registered')]"
    lstitemRegistered_xpath = "// li[contains(text(), 'Registered')]"
    lstitemRegistered_css = "body > div:nth-child(3) > div:nth-child(3) > form:nth-child(2) > section:nth-child(4) > div:nth-child(1) > div:nth-child(1) > nop-cards:nth-child(1) > nop-card:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(10) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(2) > span:nth-child(1)"
    lstitemGuests_xpath = "//li[contains(text(),'Guests')]"
    #lstitemGuests_xpath = "// li[normalize - space() = 'Guests']"
    lstitemGuests_css = "body > div:nth-child(3) > div:nth-child(3) > form:nth-child(2) > section:nth-child(4) > div:nth-child(1) > div:nth-child(1) > nop-cards:nth-child(1) > nop-card:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(10) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(3) > span:nth-child(1)"
    #lstitemVendors_xpath = "//li[contains(text(),'Vendors')]"
    lstitemVendors_xpath = "// select[ @ id = 'VendorId']"
    lstitemVendors_css = "body > div:nth-child(3) > div:nth-child(3) > form:nth-child(2) > section:nth-child(4) > div:nth-child(1) > div:nth-child(1) > nop-cards:nth-child(1) > nop-card:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(10) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(4) > span:nth-child(1)"
    #drpmgrOfVendor_xpath = "//*[@id='VendorId']"
    drpmgrOfVendor_xpath = "// select[ @ id = 'VendorId']"
    drpmgrOfVendor_css = "#VendorId"
    rdMaleGender_id = "Gender_Male"
    rdFeMaleGender_id = "Gender_Female"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtFirstName_css = "#FirstName"
    txtLastName_xpath = "//input[@id='LastName']"
    txtLastName_css = "#LastName"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtDob_css = "#DateOfBirth"
    txtCompanyName_xpath = "//input[@id='Company']"
    txtCompanyName_css = "# Company"
    txtAdminContent_xpath = "//textarea[@id='AdminComment']"
    txtAdminContent_css = "#AdminComment"
    btnSave_xpath = "//button[@name='save']"
    btnSave_css = "button[name='save'] i[class='far fa-save']"
    isTaxExempt_xpath = "//input[@class='check-box' and @id='IsTaxExempt']"
    newsLetter_xpath = "//input[@class='k-input k-readonly' and @aria-owns='SelectedNewsletterSubscriptionStoreIds_taglist SelectedNewsletterSubscriptionStoreIds_listbox']"
    managerOfVendor_xpath = "//select[@id='VendorId']"
    admin_comment_xpath = "//textarea[@class='form-control']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element(By.CSS_SELECTOR,self.lnkCustomers_menu_css).click()

    def clickOnCustomersMenuItem(self):
        self.driver.find_element(By.CSS_SELECTOR,self.lnkCustomers_menuitem_css).click()

    def clickOnAddnew(self):
        self.driver.find_element(By.CSS_SELECTOR,self.btnAddnew_css).click()

    def clickOnCustomerInfo(self):
        self.driver.find_element(By.CSS_SELECTOR,self.customerInfo_css).click()

    def setEmail(self,email):
        self.driver.find_element(By.CSS_SELECTOR,self.txtEmail_css).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.CSS_SELECTOR,self.txtPassword_css).send_keys(password)

#     def setCustomerRoles(self,role):
#         self.driver.find_element(By.XPATH,self.txtcustomerRoles_xpath).click()
#         time.sleep(3)
#         if role == 'Registered':
#             self.listitem = self.driver.find_element(By.XPATH,self.lstitemRegistered_xpath)
#         elif role=='Administrators':
#             self.listitem=self.driver.find_element(By.XPATH,self.lstitemAdministrators_xpath)
#         elif role=='Guests':
#             # Here user can be Registered( or) Guest, only one
#             time.sleep(3)
# #            self.driver.find_element(By.XPATH,"body > div:nth-child(3) > div:nth-child(3) > form:nth-child(2) > section:nth-child(4) > div:nth-child(1) > div:nth-child(1) > nop-cards:nth-child(1) > nop-card:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(10) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(1) > span:nth-child(2)").click()
#             self.listitem = self.driver.find_element(By.XPATH,self.lstitemGuests_xpath)
#         elif role=='Registered':
#             self.listitem = self.driver.find_element(By.XPATH,self.lstitemRegistered_xpath)
#         elif role=='Vendors':
#             self.listitem = self.driver.find_element(By.XPATH,self.lstitemVendors_xpath)
#         else:
#             self.listitem = self.driver.find_element(By.XPATH,self.lstitemGuests_xpath)
#         time.sleep(3)
#         self.listitem.click()
        #self.driver.execute_script("arguments[0].click();", self.listitem)

    def setCustomerRoles(self,role):
        options = self.driver.find_elements(By.XPATH,self.txtcustomerRoles_xpath)#.click()

        for option in options:
            if option.text == role:  # Replace "Option 1" with the text of the option you want to select
                option.click()
                break

    def setManagerOfVendor(self,value):
        drp=Select(self.driver.find_element(By.CSS_SELECTOR,self.drpmgrOfVendor_css))
        drp.select_by_visible_text(value)

    def setGender(self,gender):
        if gender=='Male':
            self.driver.find_element(By.ID, self.rdMaleGender_id).click()
        elif gender=='Female':
            self.driver.find_element(By.ID, self.rdFeMaleGender_id).click()
        else:
            self.driver.find_element(By.ID, self.rdMaleGender_id).click()

    def setFirstName(self, fname):
        self.driver.find_element(By.CSS_SELECTOR,self.txtFirstName_css).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.CSS_SELECTOR,self.txtLastName_css).send_keys(lname)

    def setDob(self, dob):
        self.driver.find_element(By.CSS_SELECTOR,self.txtDob_css).send_keys(dob)

    def setCompanyName(self, comname):
        self.driver.find_element(By.XPATH,self.txtCompanyName_xpath).send_keys(comname)

    def setTaxExemption(self):
        self.driver.find_element(By.XPATH, self.isTaxExempt_xpath).click()

    def setNewsLetter(self, news):
        self.driver.find_element(By.XPATH, self.newsLetter_xpath).send_keys(news)
        # newsLetterTextbox.clear()
        # newsLetterTextbox.send_keys(Keys.ENTER)

    def setManagerOfVendor(self, vendor_name):
        select_vendor= Select(self.driver.find_element(By.XPATH, self.managerOfVendor_xpath))
        select_vendor.select_by_visible_text(vendor_name)

    def setAdminComment(self, comment):
        self.driver.find_element(By.XPATH,self.admin_comment_xpath).send_keys(comment)

    def clickOnSave(self):
        self.driver.find_element(By.CSS_SELECTOR,self.btnSave_css).click()
