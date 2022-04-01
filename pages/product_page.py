from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_promo_link(self):
        assert 'promo=offer' in self.browser.current_url, "There is not promo link"
    
    def add_to_cart(self):
        button_add_to_cart = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_CART)
        button_add_to_cart.click()
    
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should not be"

    
    def should_be_message_about_adding(self):
        self.should_be_added_to_cart()
        self.should_be_cart_equal_product()


    def should_be_added_to_cart(self):
        # реализуйте проверку, что есть форма логина
        result_in_cart = self.browser.find_element(*ProductPageLocators.ADDED_TO_CART)
        name_of_product = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        assert name_of_product.text == result_in_cart.text, "There is not in cart"
    

    def should_be_cart_equal_product(self):
        # реализуйте проверку, что есть форма регистрации на странице
        result_cart = self.browser.find_element(*ProductPageLocators.PRICE_IN_CART)
        result_product = self.browser.find_element(*ProductPageLocators.PRICE_IN_PRODUCT)
        assert result_cart.text == result_product.text, "Prices don't equal"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should not be"




