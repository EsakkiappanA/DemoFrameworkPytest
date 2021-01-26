from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class BasePage:
    def enterTextToTextBox(self, webelement, text):
        self.wait.until(EC.element_to_be_clickable(webelement)).clear()
        self.wait.until(EC.visibility_of_element_located(webelement)).send_keys(
            text)
    
    def clickElement(self, webelement):
        self.wait.until(EC.visibility_of_element_located(webelement)).click()
    
    def clickElementByJavaScript(self, webelement):
        self.wait.until(EC.visibility_of_element_located(webelement))
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(*webelement))
    
    def selectFromDropDown(self, webelement, option):
        self.wait.until(EC.visibility_of_element_located(webelement))
        Select(self.driver.find_element(*webelement)).select_by_visible_text(option)
    
    def moveToElementandClick(self, webelement):
        self.wait.until(EC.visibility_of_element_located(webelement))
        ActionChains(self.driver).move_to_element(self.driver.find_element(*webelement)).click().perform()
    
        