import math

from selenium.common.exceptions import NoAlertPresentException

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def should_be_able_to_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), \
            "Item should be able to added to the cart"
        assert self.browser.find_element(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON).text == "Add to basket", \
            "Text on button should be Add to basket"

    def test_product_and_price(self):
        assert self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME).text == "Coders at Work", \
            "The name of product should be Coders at Work"
        assert self.browser.find_element(
            *ProductPageLocators.PRICE).text == "£19.99", \
            "The price of product is 19.99£"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_present_in_cart(self) -> None:
        assert self.is_element_present(
            *ProductPageLocators.PRODUCT_NAME), "Product name is not present"
        self.alert_is_presented()
        alert_text = self.browser.find_element(
            *ProductPageLocators.ALERT_ADDED_TO_CART).text
        product_name = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME).text
        assert product_name == alert_text, \
            f"The alert contains wrong product name: {alert_text} - {product_name}"

    def alert_is_presented(self):
        assert self.is_element_present(
            *ProductPageLocators.ALERT_ADDED_TO_CART
        ), "No alert that a product has been added to cart"

    def alert_is_not_presented(self):
        assert self.is_not_element_present(
                *ProductPageLocators.ALERT_ADDED_TO_CART
            ), "Alert that a product has been added to cart"

    def alert_is_disappeared(self):
        assert self.is_disappeared(
                *ProductPageLocators.ALERT_ADDED_TO_CART
            ), "Alert that a product has been added to cart"
