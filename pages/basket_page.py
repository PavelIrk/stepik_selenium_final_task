from .base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from .locators import BasketPageLocators




class BasketPage(BasePage):

    def should_be_empty_basket(self):
        assert self.browser.find_element(*BasketPageLocators.EMPTY_BUSKET), "Basket is not empty"


    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.NO_PRODUCTS), \
           "Product is presented, but should not be"


