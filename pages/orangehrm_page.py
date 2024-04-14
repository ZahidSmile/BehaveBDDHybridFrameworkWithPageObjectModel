import time
from pages.BasePage import BasePage


class OrangehrmPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.maximize_window()
        self.open_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def credentials(self):
        time.sleep(2)
        self.type_into_element('css', '[name="username"]', 'Admin')
        self.type_into_element('css', '[name="password"]', 'admin123')

    def result(self):
        self.click_on_element('css', '.orangehrm-login-button')
        time.sleep(1)
        assert self.retrieved_element_text_equals('css', '.oxd-text--h6', 'Dashboard')
