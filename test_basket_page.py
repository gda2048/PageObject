from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-age-of-the-pussyfoot_89/'
    product_page = ProductPage(browser, link)
    product_page.open()
    assert product_page.basket_price_as_str() == '0.00', 'Basket is not empty'
    product_page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    assert basket_page.check_basket_is_empty() is True, 'There are some items in the basket'
    assert basket_page.check_basket_is_not_empty() is False, 'There are some items in the basket'
