# מאפשר לנו להגדיר איך למצוא אלמנטים
from selenium.webdriver.common.by import By

# מחלקה שמאפשרת המתנה חכמה
from selenium.webdriver.support.ui import WebDriverWait

# תנאים מוכנים (visibility, clickable וכו')
from selenium.webdriver.support import expected_conditions as EC


def wait_for_element(driver, locator, timeout=10):
    """
    מחכה עד שאלמנט יהיה נראה על המסך

    driver  - הדפדפן
    locator - tuple (By, value)
    timeout - זמן המתנה מקסימלי
    """

    return WebDriverWait(driver, timeout).until(
        # מחכה עד שהאלמנט גם קיים וגם נראה
        EC.visibility_of_element_located(locator)
    )