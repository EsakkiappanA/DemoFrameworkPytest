import os
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

driver = None

@pytest.fixture(scope="module")
def setup(getBrowserName):
    global driver
    if getBrowserName == 'chrome':
        driver = webdriver.Chrome(executable_path=os.getcwd() + "/Drivers/chromedriver.exe")
    elif getBrowserName == 'firefox':
        driver = webdriver.Firefox(executable_path=os.getcwd() + "/Drivers/geckodriver.exe")
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
    wait = WebDriverWait(driver, 10)
    yield driver, wait
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="module")
def getBrowserName(request):
    return request.config.getoption("--browser")