from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def check_basket_is_empty(self):
        return self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS)

    def check_basket_is_not_empty(self):
        return self.is_element_present(*BasketPageLocators.BASKET_ITEMS)
