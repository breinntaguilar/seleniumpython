from Locators.locators import Locators

class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        self.email_textbox_name = Locators.email_textbox_name
        self.password_textbox_name = Locators.password_textbox_name
        self.login_button_class = Locators.login_button_class
        self.error_alert_xpath = Locators.error_alert_xpath
        self.error_list_class = Locators.error_list_class
        self.forgot_password_class = Locators.forgot_password_class
        self.forgot_password_popup_email = Locators.forgot_password_popup_email
        self.forgot_password_popup_submit = Locators.forgot_password_popup_submit
        self.forgot_password_popup_info_message = Locators.forgot_password_popup_info_message

    def enter_email(self, email):
        self.driver.find_element_by_name(self.email_textbox_name).clear()
        self.driver.find_element_by_name(self.email_textbox_name).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element_by_name(self.password_textbox_name).clear()
        self.driver.find_element_by_name(self.password_textbox_name).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_class_name(self.login_button_class).click()

    def click_login_invalid_email(self):
        self.driver.find_element_by_class_name(self.login_button_class).click()
        element = self.driver.find_element_by_xpath(self.error_alert_xpath)
        assert "Please, enter valid credentials" in element.text

    def click_login_invalid_password(self):
        self.driver.find_element_by_class_name(self.login_button_class).click()
        element = self.driver.find_element_by_xpath(self.error_alert_xpath)
        assert "Please, enter valid credentials" in element.text

    def click_login_invalid_empty_fields(self):
        self.driver.find_element_by_class_name(self.login_button_class).click()
        element = self.driver.find_element_by_class_name(self.error_list_class)
        assert "This is a required field" in element.text

    def click_forgot_password(self, email):
        self.driver.find_element_by_class_name(self.forgot_password_class).click()
        self.driver.find_element_by_xpath(self.forgot_password_popup_email).clear()
        self.driver.find_element_by_xpath(self.forgot_password_popup_email).send_keys(email)

    def click_forgot_password_popup_submit(self):
        self.driver.find_element_by_xpath(self.forgot_password_popup_submit).click()
        element = self.driver.find_element_by_xpath(self.forgot_password_popup_info_message)
        assert "If the email address provided is in the database, an email will be sent with further instructions to reset the password." in element.text
