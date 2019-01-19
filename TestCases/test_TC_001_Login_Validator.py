from Base import InitiateDriver
from Pages import LoginPage
import pytest
from DataGenerator import DataGen


@pytest.mark.parametrize('data',DataGen.dataGenerator())
def test_LoginValidation(data):
    driver = InitiateDriver.startBrowser()
    login = LoginPage.LoginClass(driver)
    login.enter_username(data[0])
    login.enter_password(data[1])
    driver.close()


