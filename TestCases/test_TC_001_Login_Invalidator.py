from Base import InitiateDriver
from Pages import LoginPage

def test_LoginInvalidation():
    driver = InitiateDriver.startBrowser()
    login = LoginPage.LoginClass(driver)
    login.enter_email("palpapvijay@gmail.com")
    driver.close()
