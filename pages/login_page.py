from .base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.browser.current_url, "There is not login link"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM), "There is not login form"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.browser.find_element(*LoginPageLocators.REGISTER_FORM), "There is not register form"

    def register_new_user(self, email, password):
        # регистрируем нового пользователя
        button_login_link = self.browser.find_element(*LoginPageLocators.LOGIN_LINK)
        button_login_link.click()
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        email_field.send_keys(email)
        password_field1 = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD1)
        password_field1.send_keys(password)
        password_field2 = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD2)
        password_field2.send_keys(password)
        button_registr = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTR)
        button_registr.click()
        



