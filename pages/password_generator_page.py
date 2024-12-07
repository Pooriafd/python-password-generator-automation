from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class PasswordGeneratorPage(BasePage):
    length_input = (By.ID, "passwordLength")
    generate_button = (By.CSS_SELECTOR, "button[title='Generate password']")
    copy_button = (By.CSS_SELECTOR, "button[title='Copy Password']")
    password_output = (By.CSS_SELECTOR, "input#password")
    checkboxes = {
        "lowercase": (By.CSS_SELECTOR, "input#option-lowercase"),
        "uppercase": (By.CSS_SELECTOR, "input#option-uppercase"),
        "numbers": (By.CSS_SELECTOR, "input#option-numbers"),
        "symbols": (By.CSS_SELECTOR, "input#option-symbols"),  # Assuming you have an 'option-symbols' checkbox
    }

    def set_length(self, length):
        self.send_keys(self.length_input, str(length))

    def toggle_option(self, option, state):
        checkbox = self.find_element(self.checkboxes[option])
        if checkbox.is_selected() != state:
            checkbox.click()

    def click_generate_button(self):
        self.click(self.generate_button)

    def get_generated_password(self):
        return self.get_attribute(self.password_output, "value")

    def wait_for_copy_button(self):
        """Waits for the 'Copy Password' button to be visible"""
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.copy_button)
        )
