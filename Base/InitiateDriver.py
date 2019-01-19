from selenium import webdriver
from Lib import configReader
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def startBrowser():
    global driver

    if(configReader.readConfigData('Details','Browser')) == "chrome":
        path = "./Drivers/chromedriver.exe"
        driver = webdriver.Chrome(executable_path=path)
    elif(configReader.readConfigData('Details','Browser')) == "firefox":
        path = "./Drivers/geckodriver.exe"
        cap = DesiredCapabilities().FIREFOX
        cap["marionette"] = False
        driver = webdriver.Firefox(capabilities=cap,executable_path=path)
    elif(configReader.readConfigData('Details','Browser')) == "ie":
        path = "./Drivers/IEDriverServer.exe"
        driver = webdriver.Ie(executable_path=path)
    else:
        path = "./Drivers/chromedriver.exe"
        driver = webdriver.Chrome(executable_path=path)

    driver.get(configReader.readConfigData('Details','Application_URL'))
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver

def closeBrowser():
    driver.close()
    driver.quit()