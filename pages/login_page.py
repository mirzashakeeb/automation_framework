from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.url = "https://www.saucedemo.com/"

    # Open login page
    def open(self):
        self.driver.get(self.url)

    # Enter username and password
    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    # Check if login was successful
    def is_logged_in(self):
        return "inventory.html" in self.driver.current_url
