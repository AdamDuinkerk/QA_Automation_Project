# מאפשר לבחור אלמנטים לפי ID / CSS וכו'
from selenium.webdriver.common.by import By

# פונקציית wait שכתבנו
from utils.waits import wait_for_element


class LoginPage:
    def __init__(self, driver):
        # שמירת הדפדפן לשימוש בכל המתודות
        self.driver = driver

    # === Locators ===
    username = (By.ID, "user-name")  # שדה שם משתמש
    password = (By.ID, "password")  # שדה סיסמה
    login_button = (By.ID, "login-button")  # כפתור login
    error_message = (By.CSS_SELECTOR, "h3[data-test='error']")  # הודעת שגיאה

    def login(self, user, pwd):
        """
        מבצע התחברות למערכת
        """

        # מחכה לשדה username ואז מקליד
        wait_for_element(self.driver, self.username).send_keys(user)

        # מחכה לשדה password ואז מקליד
        wait_for_element(self.driver, self.password).send_keys(pwd)

        # מחכה לכפתור login ולוחץ
        wait_for_element(self.driver, self.login_button).click()

    def get_error(self):
        """
        מחזיר טקסט של הודעת שגיאה
        """
        return wait_for_element(self.driver, self.error_message).text