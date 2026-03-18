import pytest
from utils.driver_factory import get_driver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()


def test_add_to_cart(driver):
    """
    בדיקה של הוספת מוצר לסל
    """

    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)

    # מוסיף מוצר
    inventory_page.add_first_item_to_cart()

    # בודק שנוסף לסל
    assert inventory_page.get_cart_count() == "1"


def test_products_exist(driver):
    """
    בדיקה שיש מוצרים בדף
    """

    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)

    items = inventory_page.get_item_names()

    # בודק שיש לפחות מוצר אחד
    assert len(items) > 0