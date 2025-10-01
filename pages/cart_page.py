from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        # Locators
        self.cart_button = (By.ID, "cart-button")  # Example: Cart icon/button
        self.checkout_button = (By.ID, "checkout")  # Checkout button
        self.items_in_cart = (By.CSS_SELECTOR, ".cart_item")  # All cart items
        self.remove_buttons = (By.CSS_SELECTOR, ".cart_item button.remove")  # Remove buttons

    # Go to cart page
    def open_cart(self):
        self.driver.find_element(*self.cart_button).click()

    # Get number of items in cart
    def get_item_count(self):
        return len(self.driver.find_elements(*self.items_in_cart))

    # Remove item by index
    def remove_item(self, index=0):
        buttons = self.driver.find_elements(*self.remove_buttons)
        if index < len(buttons):
            buttons[index].click()

    # Proceed to checkout
    def checkout(self):
        self.driver.find_element(*self.checkout_button).click()
