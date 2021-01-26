from time import sleep

from selenium.webdriver.support import expected_conditions as EC
from Pages.LoginPage import loginPage


class Test_login:
    def test_verifytTitle(self,setup):
        self.driver,self.wait=setup
        assert self.wait.until(EC.title_is('OrangeHRM'))
        
    def test_verifyLogin(self,setup):
        self.driver, self.wait = setup
        lgPage=loginPage(self.driver,self.wait)
        lgPage.enterTextToTextBox(loginPage.usernameTextBox,"Admin")
        lgPage.enterTextToTextBox(loginPage.passwordTextBox,"admin123")
        lgPage.clickElement(loginPage.loginButton)
        assert self.wait.until(EC.title_is('OrangeHRM')),"Login Failed"