from selenium.webdriver.common.by import By

from configs.support_date import chars_convert_from_calc, chars_convert_in_calc
from page.BasePage import BasePage


class Locators:
    LOCATOR_CALC_INPUT = (By.XPATH, "//div[@class='jlkklc']")
    LOCATOR_CALC_HISTORY_FIELD = (By.CLASS_NAME, "vUGUtc")

    LOCATOR_CALC_NUMPAD_BUTTONS = (
        By.XPATH, "//table[@class='ElumCf']//div[@role='button' and not(contains(@style,'display:none'))]")

    LOCATOR_CALC_enter = (
        By.XPATH, '//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[5]/td[3]/div/div')


class GoogleCalculator(BasePage):
    def _click_enter(self):
        return self.find_element(Locators.LOCATOR_CALC_enter).click()

    def send_numpad(self, prem):
        """Ввод мат.примера"""
        self.numpad_buttons = self.find_elements(Locators.LOCATOR_CALC_NUMPAD_BUTTONS)

        self.text_list = prem
        for i in self.text_list:
            if i in chars_convert_in_calc:
                self.text_list = self.text_list.replace(i, chars_convert_in_calc[i])

        for char in self.text_list.split():
            for self.button in self.numpad_buttons:
                if self.button.text == char:
                    self.button.click()

        return self._click_enter()

    def get_history(self) -> str:
        """Возвращает историю операций из калькулятора"""
        calculator_history = self.find_element(Locators.LOCATOR_CALC_HISTORY_FIELD).text

        for char in calculator_history:
            if char in chars_convert_from_calc:
                calculator_history = calculator_history.replace(char, chars_convert_from_calc[char])

        return calculator_history

    def get_result(self) -> str:
        """Возвращает результат из калькулятора"""
        return self.find_element(Locators.LOCATOR_CALC_INPUT).text
