import time

import pytest

from .links import CATALOGUE_207_LINK
from .links import CATALOGUE_209_LINK
from .links import CATALOGUE_95_LINK
from .links import LOGIN_LINK
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage

offers = [f"{CATALOGUE_207_LINK}/?promo=offer{n}" for n in [0, 1, 2, 3, 4, 5, 6, 8, 9]]
offers += [pytest.param(f"{CATALOGUE_207_LINK}/?promo=offer7", marks=pytest.mark.xfail)]


@pytest.mark.parametrize('link', offers)
def test_guest_can_add_product_to_basket_coders_at_work(browser, link):
    browser.delete_all_cookies()
    page = ProductPage(browser, link)
    page.open()
    page.test_product_and_price()
    page.should_be_able_to_add_to_basket()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_present_in_cart()


@pytest.mark.to_basket_from_product
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        login_page = LoginPage(browser, LOGIN_LINK)
        login_page.open()
        email = str(time.time()) + "@fakemail.org"
        login_page.register_new_user(email, 'passwordWOW23')
        login_page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, f'{CATALOGUE_209_LINK}?promo=newYear')
        page.open()
        page.should_be_able_to_add_to_basket()
        page.add_to_basket()
        page.solve_quiz_and_get_code()

    def test_user_cant_see_success_message(self, browser):
        link = CATALOGUE_207_LINK
        page = ProductPage(browser, link)
        page.open()
        page.alert_is_not_presented()


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, f'{CATALOGUE_209_LINK}?promo=newYear')
    page.open()
    page.should_be_able_to_add_to_basket()
    page.add_to_basket()
    page.solve_quiz_and_get_code()


@pytest.mark.need_review
@pytest.mark.xfail
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, CATALOGUE_207_LINK)
    page.open()
    page.add_to_basket()
    page.alert_is_not_presented()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, CATALOGUE_207_LINK)
    page.open()
    page.add_to_basket()
    page.alert_is_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, CATALOGUE_95_LINK)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, CATALOGUE_95_LINK)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
