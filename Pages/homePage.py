from Locators.locators import Locators

class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.logout_button_class = Locators.logout_button_class

    def click_logout(self):
        self.driver.find_element_by_class_name(self.logout_button_class).click()
