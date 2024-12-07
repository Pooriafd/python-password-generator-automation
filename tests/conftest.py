import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def driver():
    ChromeDriverManager().install()
    driver = webdriver.Chrome()  # Set up ChromeDriver
    driver.maximize_window()  # Maximize browser window for consistent behavior
    yield driver  # Provide the WebDriver to the test
    driver.quit()  # Teardown: close the browser after the test
