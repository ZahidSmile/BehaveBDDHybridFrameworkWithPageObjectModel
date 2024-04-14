import time
from selenium.webdriver.common.keys import Keys
from pages.BasePage import BasePage


class GoogleSearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def goto_google(self):
        self.driver.maximize_window()
        self.open_url("https://www.google.com")

    def search(self, keyword):
        search_field = self.get_element('css', '#APjFqb')
        search_field.send_keys(keyword)
        search_field.send_keys(Keys.RETURN)

    def is_search_results_present(self):
        time.sleep(1)
        assert self.retrieved_element_text_equals('css', '.LC20lb.MBeuO.DKV0Md', 'Selenium')
