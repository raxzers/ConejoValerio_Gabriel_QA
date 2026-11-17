

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options



from pages.login_page import LoginPage  # noqa: E402

APPIUM_SERVER_URL = "http://localhost:4723"

CAPABILITIES = {
    "platformName": "Android",
    "appium:automationName": "UiAutomator2",
    "appium:deviceName": "Pixel 4 API 34",
    "appium:platformVersion": "14.0",
    "appium:appPackage": "com.shopgo.app",        # ejemplo
    "appium:appActivity": ".ui.LoginActivity",    # ejemplo
}


@pytest.fixture(scope="function")
def driver():
    """Crea el driver de Appium antes de cada prueba y lo cierra al terminar."""
    options = UiAutomator2Options().load_capabilities(CAPABILITIES)
    driver = webdriver.Remote(APPIUM_SERVER_URL, options=options)
    yield driver
    driver.quit()


@pytest.fixture
def login_page(driver):
    return LoginPage(driver)