from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from time import sleep

from Test_data import credentials
from Test_locators.test_locators import LoginPageLocators

class LoginPageActions:
    def __init__(self):
        self.loginlocators = LoginPageLocators()
        self.driver = webdriver.Chrome()
        self.driver.get(credentials.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def enter_username(self):
        """
        find the webelement for username ,clear the text field and set the username passed

        :return:
        """
        username_webelement = self.driver.find_element(By.NAME, self.loginlocators.username_locator_name_tag)
        username_webelement.clear()
        username_webelement.send_keys(credentials.username)
        print("Username entered")

    def enter_password(self):
        """
        find the webelement for password ,clear the text field and set the username passed
        :return:
        """
        password_webelement = self.driver.find_element(By.NAME, self.loginlocators.password_locator_name_tag)
        password_webelement.clear()
        password_webelement.send_keys(credentials.password)
        print("password entered")

    def click_login(self):
        login_button_webelement = self.driver.find_element(By.XPATH, self.loginlocators.login_button)
        login_button_webelement.click()
        print("Login button clicked")

    def title_of_page(self):
        title_name = self.driver.title
        print("Returning title of webpage", title_name)
        return self.driver.title

    def login_to_automationExercise(self):
        self.enter_username()
        self.enter_password()
        self.click_login()
        self.driver.implicitly_wait(5)

# if __name__ == '__main__':
#     LoginPageActions().login_to_orangehrm()