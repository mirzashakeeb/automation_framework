import pytest
from pages.login_page import LoginPage
from utils.driver_factory import get_driver
import allure

@allure.feature("Login")
@allure.story("Valid Login")
def test_login():
    driver = get_driver()
    login_page = LoginPage(driver)
    login_page.open()  # <-- replaced go_to_login() with open()
    login_page.login("standard_user", "secret_sauce")
    assert login_page.is_logged_in()
    driver.quit()
