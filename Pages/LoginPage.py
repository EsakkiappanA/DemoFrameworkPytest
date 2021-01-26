from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class loginPage(BasePage):
    usernameTextBox = (By.ID,"txtUsername")
    passwordTextBox = (By.ID,"txtPassword")
    loginButton = (By.ID,"btnLogin")
    
    def __init__(self,driver, wait):
        self.driver = driver
        self.wait = wait
        
    
    