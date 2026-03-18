import pytest
from utils.driver_factory import get_driver
from pages.login_page import LoginPage


@pytest.fixture
def driver():
    """
    fixture שמטפל בפתיחה וסגירה של הדפדפן
    """
    driver = get_driver()
    yield driver
    driver.quit()


def test_valid_login(driver):
    """
    בדיקת התחברות תקינה
    """

    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    # בדיקה שעברנו לעמוד inventory
    assert "inventory" in driver.current_url


def test_invalid_login(driver):
    """
    בדיקת התחברות שגויה
    """

    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)
    login_page.login("invalid_user", "wrong_password")

    # בדיקה שמופיעה הודעת שגיאה
    assert "Epic sadface" in login_page.get_error()