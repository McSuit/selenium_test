from pages.cart_page import CartPage
from pages.catalog_iphone import CatalogIphonePage
from pages.main_page import MainPage
from utilities.conftest import *

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.page_load_strategy = 'eager'
base_driver = webdriver.Chrome(options=chrome_options)


def test_buy_iphone(set_group, set_up):
    mp = MainPage(base_driver)
    mp.open_url('https://pitergsm.ru/')
    mp.print_current_url()
    mp.click_iphone_button()

    cp = CatalogIphonePage(base_driver)
    cp.print_current_url()
    cp.select_black_15_pro_max_120k()

    name_modal = cp.get_modal_product_name().text
    price_modal = cp.get_modal_product_price().text[:7]

    cart = CartPage(base_driver)
    cart.print_current_url()
    cart.print_cart_product_name()
    cart.print_cart_product_price()

    name_cart = cart.get_cart_product_name().text
    price_cart = cart.get_cart_product_price().text

    print('assert product name value')
    cart.assert_value(name_modal, name_cart)
    print('assert product price value')
    cart.assert_value(price_modal, price_cart)

    cart.click_cart_order_button()

    print('assert url')
    cart.assert_url('https://pitergsm.ru/personal/order/make/')

    cart.make_screenshot()
