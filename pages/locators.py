from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, '//div[contains(@class, "basket-mini")]/span/a')
    BASKET_PRICE = (By.CLASS_NAME, 'basket-mini')


class BasketPageLocators:
    BASKET_ITEMS = (By.CLASS_NAME, 'basket-items')


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, 'btn-add-to-basket')
    PRODUCT_NAME = (By.XPATH, '//div[contains(@class, "product_main")]/h1')
    PRICE = (By.XPATH, '//div[@class="col-sm-6 product_main"]/p[@class="price_color"]')
    ALERT_ADDED_TO_CART = (By.CSS_SELECTOR, "div.alertinner strong")
