import os
import pytest

from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    # driver = webdriver.Chrome(executable_path=os.getcwd() + '/drivers/chromedriver')
    driver = webdriver.Chrome(executable_path='/home/glyntwain/Документы/Test-task-for-SimbirSoft/drivers/chromedriver')

    yield driver
    driver.close()
    driver.quit()
