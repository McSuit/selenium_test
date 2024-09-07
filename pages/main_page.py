
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


class MainPage(Base):
    """Класс главной страницы"""
    def __init__(self, driver):
        super().__init__(driver)

    # Locators

    iphone_button = '//*[@id="js-drop-header"]/div[2]/ul/li[1]/a'

    # Getters
    def get_iphone_button(self):
        return WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable
                                                    ((By.XPATH, self.iphone_button)))
    # Actions

    def click_iphone_button(self):
        self.get_iphone_button().click()
        print('click iphone button')
