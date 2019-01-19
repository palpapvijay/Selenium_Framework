from Lib import configReader

class LoginClass():

    def __init__(self,obj):
        global driver
        driver = obj


    def enter_username(self,username):
        driver.find_element_by_name(configReader.fetchElementLocators("Login", "username_name")).send_keys(username)

    def enter_password(self,password):
        driver.find_element_by_name(configReader.fetchElementLocators("Login", "email_name")).send_keys(password)

    def enter_email(self,email):
        driver.find_element_by_name(configReader.fetchElementLocators("Login", "password_name")).send_keys(email)