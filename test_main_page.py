import pytest

from .links import MAIN_PAGE_LINK
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.main_page import MainPage


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, MAIN_PAGE_LINK)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        page = MainPage(browser, MAIN_PAGE_LINK)
        page.open()
        page.basket_price_is_zero()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.check_basket_is_empty()
        basket_page.check_basket_is_not_empty()
