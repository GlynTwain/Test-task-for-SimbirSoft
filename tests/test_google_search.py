import pytest

from page.GoogleSearchPage import GoogleSearch
from page.GoogleCalculatorPage import GoogleCalculator


@pytest.mark.parametrize("example, result", [
    ("1 * 2 - 3 + 1", '0')
])
def test_google_calc(browser, example, result):
    """Кейс проверки калькулятора"""
    google_main_page = GoogleSearch(browser)
    google_main_page.go_url('http://www.google.com')
    google_main_page.enter_word("калькулятор")
    google_main_page.click_on_the_search_button()

    calc = GoogleCalculator(browser)
    calc.send_numpad(example)

    calc_result = calc.get_result()
    calc_history = calc.get_history()

    assert calc_result == result
    assert calc_history == example + ' ='
