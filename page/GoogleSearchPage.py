from selenium.webdriver.common.by import By

from configs.main_config import MINIMAL_WAIT_TIME
from page.BasePage import BasePage


class GS_Locators:
    LOCATOR_GOOGLE_SEARCH_FIELD = (By.XPATH, "//input[@name='q']")
    LOCATOR_GOOGLE_SEARCH_BUTTON = (By.XPATH, "(//input[@name='btnK'])[1]")  # (By.CLASS_NAME, "gNO89b")


class GoogleSearch(BasePage):

    def enter_word(self, search_text: str):
        """Ввести слово в строку поиска Google"""
        search_field = self.find_element(GS_Locators.LOCATOR_GOOGLE_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(search_text)
        return search_field

    def click_on_the_search_button(self):
        """В выпадающем окне нажать Поиск в Гугл"""
        return self.find_element(GS_Locators.LOCATOR_GOOGLE_SEARCH_BUTTON, time=MINIMAL_WAIT_TIME).click()
