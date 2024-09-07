import datetime


class Base:
    """Базовый класс для страниц"""
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):  # открывает заданный url
        self.driver.get(url)
        self.driver.maximize_window()

    def print_current_url(self):  # выводит текущий URL
        url = self.driver.current_url
        print(f'current url {url}')

    def make_screenshot(self):  # делает скриншот
        utc_time = datetime.datetime.now().strftime('%d.%m.%Y_%H.%M.%S')
        screen_name = str(utc_time) + '.png'
        self.driver.save_screenshot('./screen' + screen_name)
        print('screenshot made')

    def assert_value(self, value, result):  # проверяет соответствие слова
        assert value == result
        print('value assertion success')

    def assert_url(self, result):  # проверяет соответствие url
        url = self.driver.current_url
        assert url == result
        print('url assertion success')