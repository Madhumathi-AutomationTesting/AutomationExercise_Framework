from selenium import webdriver
from selenium.webdriver.common.by import By

from PageObjects.login_page_POM import LoginPageActions
from Test_data import credentials
from Test_locators.test_locators import LoginPageLocators

class TestLoginTitle:
    # def __init__(self):
    #     pass

    def test_login_page_title(self):
        """
        Testcase to test the title of our webpage
        :return:
        """
        expected_title = "OrangeHRM"

        LoginPageActions().login_to_automationExercise()
        assert LoginPageActions().title_of_page() == expected_title

# TestLoginTitle().test_login_page_title()

