import pytest
from pages.cart_page import CartPage
from pages.login_page import LoginPage
from utils.driver_factory import get_driver
import allure

@allure.feature("Cart")
@allure.story("Add and Remove Items")
def test_cart_operations():
    driver = get_driver()

    # Login first
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    cart_page = CartPage(driver)
    cart_page.open_cart()

    # Check items
    initial_count = cart_page.get_item_count()
    print(f"Items in cart: {initial_count}")

    # Remove first item if exists
    if initial_count > 0:
        cart_page.remove_item(0)
        assert cart_page.get_item_count() == initial_count - 1

    driver.quit()
