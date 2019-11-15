import unittest
from selenium import webdriver
import time
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"...","..."))
from Pages.loginPage import LoginPage
from Pages.homePage import HomePage
import HtmlTestRunner

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driverLocation = "/Users/breinn.aguilar/PycharmProjects/chromedriver"
        os.environ["webdriver.chrome.driver"] = cls.driverLocation
        cls.driver = webdriver.Chrome(cls.driverLocation)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        driver.get("http://medechat-client.qa.butterfly.com.au/")

        login = LoginPage(driver)
        login.enter_email("breinn.aguilar@butterfly.com.au")
        login.enter_password("But3as2flying")
        login.click_login()
        time.sleep(2)

        homepage = HomePage(driver)
        homepage.click_logout()

    def test_login_invalid_email(self):
        driver = self.driver
        driver.get("http://medechat-client.qa.butterfly.com.au/")

        login = LoginPage(driver)
        login.enter_email("breinn.aguilar@butterfly.com")
        login.enter_password("But3as2flying")
        login.click_login_invalid_email()
        time.sleep(2)

    def test_login_invalid_password(self):
        driver = self.driver
        driver.get("http://medechat-client.qa.butterfly.com.au/")

        login = LoginPage(driver)
        login.enter_email("breinn.aguilar@butterfly.com.au")
        login.enter_password("But3as2flying!")
        login.click_login_invalid_password()
        time.sleep(2)

    def test_login_invalid_empty_fields(self):
        driver = self.driver
        driver.get("http://medechat-client.qa.butterfly.com.au/")

        login = LoginPage(driver)
        login.enter_email("")
        login.enter_password("")
        login.click_login_invalid_empty_fields()
        time.sleep(2)

    def test_login_forgot_password(self):
        driver = self.driver
        driver.get("http://medechat-client.qa.butterfly.com.au/")

        login = LoginPage(driver)
        login.click_forgot_password("breinn+PM1@gmail.com")
        login.click_forgot_password_popup_submit()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

if __name__ == '__main__':
        unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/breinn.aguilar/PycharmProjects/Medechat/reports'))
