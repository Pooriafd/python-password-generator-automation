import pytest
from pages.password_generator_page import PasswordGeneratorPage

@pytest.fixture
def setup(driver):
    driver.get("https://www.security.org/password-generator/")
    page = PasswordGeneratorPage(driver)
    page.wait_for_copy_button()
    return page

def test_minimum_length(setup):
    page = setup
    page.set_length(1)
    page.toggle_option("lowercase", True)
    page.click_generate_button()
    password = page.get_generated_password()
    assert len(password) == 6

def test_only_uppercase(setup):
    page = setup
    page.set_length(10)
    page.toggle_option("uppercase", True)
    page.toggle_option("lowercase", False)
    page.toggle_option("numbers", False)
    page.toggle_option("symbols", False)
    page.click_generate_button()
    password = page.get_generated_password()
    assert password.isupper()
