import os
import pytest

from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    path_driver = os.path.abspath('../drivers/chromedriver')
    driver = webdriver.Chrome(executable_path=path_driver)
    yield driver
    driver.close()
    driver.quit()
