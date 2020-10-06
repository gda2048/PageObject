from .links import CATALOGUE_89_LINK
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    product_page = ProductPage(browser, CATALOGUE_89_LINK)
    product_page.open()
    product_page.basket_price_is_zero()
    product_page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.check_basket_is_not_empty()
    basket_page.check_basket_is_empty()
