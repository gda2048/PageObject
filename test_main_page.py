import pytest

from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.main_page import MainPage


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        assert page.basket_price_as_str() == '0.00', 'Basket is not empty'
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        assert basket_page.check_basket_is_empty() is True, 'There are some items in the basket'
        assert basket_page.check_basket_is_not_empty() is False, 'There are some items in the basket'
