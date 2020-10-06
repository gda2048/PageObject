from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def check_basket_is_empty(self):
        is_not_presented = self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS)
        assert is_not_presented is True, 'There are some items in the basket'

    def check_basket_is_not_empty(self):
        is_presented = self.is_element_present(*BasketPageLocators.BASKET_ITEMS)
        assert is_presented is False, 'There are some items in the basket'
