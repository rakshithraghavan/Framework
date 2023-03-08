from selenium.webdriver.common.by import By
class LoginPage:
    textbox_username_id="Email"
    textbox_password_id="Password"
    #button_login_xpath="//body[1]/div[6]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[3]/button[1]"
    #button_login_xpath ="//input[#class='button-1 login-button']"
    button_login_tag="button"
    link_logout_linktext="Logout"
#'"//body[1]/div[6]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[3]/button[1]" \
#"://body[1]/div[3]/nav[1]/div[1]/ul[1]/li[3]/a[1]"

    def __init__(self,driver):
        self.driver=driver

    def setUserName(self,username):
        self.driver.find_element(By.ID,self.textbox_username_id).clear()
        inputEmail=self.driver.find_element(By.ID,self.textbox_username_id)
        inputEmail.send_keys(username)
    def setPassword(self, password):
        self.driver.find_element(By.ID,self.textbox_password_id).clear()
        inputPassword=self.driver.find_element(By.ID,self.textbox_password_id)
        inputPassword.send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.TAG_NAME,self.button_login_tag).click()

    def clickLogout(self):
#        self.driver.find_element_by_link_text(self.link_logout_linktext).click()
        self.driver.find_element(By.LINK_TEXT, self.link_logout_linktext).click()



