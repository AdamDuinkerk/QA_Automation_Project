from selenium.webdriver.common.by import By
from utils.waits import wait_for_element


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    # === Locators ===
    inventory_items = (By.CLASS_NAME, "inventory_item")  # כל המוצרים
    add_to_cart_button = (By.CSS_SELECTOR, "button.btn_inventory")  # כפתורי add
    cart_badge = (By.CLASS_NAME, "shopping_cart_badge")  # מספר פריטים בסל

    def add_first_item_to_cart(self):
        """
        מוסיף את המוצר הראשון לסל
        """

        # מוצא את כל כפתורי add to cart
        buttons = self.driver.find_elements(*self.add_to_cart_button)

        # לוחץ על הראשון ברשימה
        buttons[0].click()

    def get_cart_count(self):
        """
        מחזיר כמה פריטים יש בסל
        """

        # מחכה לאייקון הסל ומחזיר את המספר
        return wait_for_element(self.driver, self.cart_badge).text

    def get_item_names(self):
        """
        מחזיר רשימה של שמות המוצרים
        """

        # מוצא את כל שמות המוצרים
        items = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")

        # מחזיר רשימה של טקסטים
        return [item.text for item in items]