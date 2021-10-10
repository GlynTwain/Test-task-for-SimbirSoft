import os
import pytest

from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    path_driver = os.path.abspath('../drivers/chromedriver')  # Используеммая версия - 94.0.4606.61
    driver = webdriver.Chrome(executable_path=path_driver)
    yield driver
    driver.close()
    driver.quit()
