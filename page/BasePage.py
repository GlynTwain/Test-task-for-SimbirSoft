from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from configs.main_config import STANDART_WAIT_TIME


# Базовый класс от которого наследуются все страницы
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time: int = STANDART_WAIT_TIME):
        """Найти элемент"""
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Не могу найти элемент по локатору {locator}")

    def find_elements(self, locator, time: int = STANDART_WAIT_TIME):
        """Найти элементы"""
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Не могу найти элементы по локатору {locator}")

    def go_url(self, url: str):
        """Перети по адресу"""
        return self.driver.get(url)
