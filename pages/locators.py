from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BUTTON_BASKET = (By.CSS_SELECTOR, ".btn-group .btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")    
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_FIELD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_FIELD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON_REGISTR = (By.CSS_SELECTOR, "#register_form > button")
    SUCCSES_REGISTR = (By.CSS_SELECTOR, ".icon-ok-sign")
    
class ProductPageLocators():
    BUTTON_ADD_TO_CART = (By.CSS_SELECTOR, "#add_to_basket_form")
    ADDED_TO_CART = (By.CSS_SELECTOR, ".alertinner strong")
    PRICE_IN_CART = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRICE_IN_PRODUCT = (By.CSS_SELECTOR, "p.price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div .alertinner")

class BasketPageLocators():
    EMPTY_BUSKET = (By.CSS_SELECTOR, "#content_inner p")
    NO_PRODUCTS = (By.CSS_SELECTOR, ".price_color")

    
