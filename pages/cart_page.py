from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


class CartPage(Base):

    def __init__(self, driver):
        super().__init__(driver)

    # Locators

    cart_product_name = '//div[@class="cart-prod__title"]'
    cart_product_price = '//strong[@id="total-summ-place"]'
    cart_order_button = '//span[@class="nomobile"]'

    # Getters

    def get_cart_product_name(self):
        return WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable
                                                    ((By.XPATH, self.cart_product_name)))

    def get_cart_product_price(self):
        return WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable
                                                    ((By.XPATH, self.cart_product_price)))

    def get_cart_order_button(self):
        return WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable
                                                    ((By.XPATH, self.cart_order_button)))
    # Actions

    def print_cart_product_name(self):
        name_cart = self.get_cart_product_name().text
        print(f'cart product name: {name_cart}')

    def print_cart_product_price(self):
        price_cart = self.get_cart_product_price().text
        print(f'cart product price: {price_cart}')

    def click_cart_order_button(self):
        self.get_cart_order_button().click()
        print('click cart order button')
