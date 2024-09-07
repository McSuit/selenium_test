import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


class CatalogIphonePage(Base):
    """Класс страницы Iphone каталога"""
    def __init__(self, driver):
        super().__init__(driver)

    # Locators

    button_15_pro_max = '//a[text()="iPhone 15 Pro Max"]'
    max_price = '//input[@name="arrFilter_P1_MAX"]'
    checkbox_black = '//span[text()="Чёрный "]'
    button_buy = '//span[text()="Купить"]'
    modal_product_name = '//div[@class="cart-prod__title"]'
    modal_product_price = '//div[@class="cart-prod__summ"]'
    modal_button_buy = '//a[text()="В корзину"]'

    # Getters

    def get_button_15_pro_max(self):
        return WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable
                                                    ((By.XPATH, self.button_15_pro_max)))

    def get_max_price(self):
        return WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable
                                                ((By.XPATH, self.max_price)))

    def get_checkbox_black(self):
        return WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable
                                                ((By.XPATH, self.checkbox_black)))

    def get_button_buy(self):
        return WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable
                                                ((By.XPATH, self.button_buy)))

    def get_modal_product_name(self):
        return WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable
                                                ((By.XPATH, self.modal_product_name)))

    def get_modal_product_price(self):
        return WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable
                                                ((By.XPATH, self.modal_product_price)))

    def get_modal_button_buy(self):
        return WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable
                                                ((By.XPATH, self.modal_button_buy)))

    # Actions

    def click_button_15_pro_max(self):
        self.get_button_15_pro_max().click()
        print('click button 15 pro max')

    def input_max_price(self, price):
        self.get_max_price().click()
        self.get_max_price().clear()
        self.get_max_price().send_keys(price)
        print(f'input max price {price}')

    def click_checkbox_black(self):
        self.get_checkbox_black().click()
        print('click checkbox black')

    def click_button_buy(self):
        self.get_button_buy().click()
        print('click button buy')

    def print_modal_product_name(self):
        name_modal = self.get_modal_product_name().text
        print(f'product name: {name_modal}')

    def print_modal_product_price(self):
        price_modal = self.get_modal_product_price().text[:7]
        print(f'product price: {price_modal}')

    def click_modal_button_buy(self):
        self.get_modal_button_buy().click()
        print('click modal button buy')

    # Methods

    def select_black_15_pro_max_120k(self):
        self.click_button_15_pro_max()
        self.input_max_price(120000)
        self.driver.execute_script("window.scrollTo(0, 2000);")
        self.click_checkbox_black()
        self.driver.execute_script("window.scrollTo(0, 500);")
        time.sleep(5)  # без ожидания часто выпадает StaleElementReferenceException
        self.click_button_buy()
        self.print_modal_product_name()
        self.print_modal_product_price()
        self.click_modal_button_buy()
