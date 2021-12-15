from selenium.webdriver.common.by import By

class SecurePage:
    #locators
    USERNAME_FIELD =(By.ID, 'username')
    PASSWORD_FIELD =(By.ID, 'password')
    #LOGIN_BUTTON =(By.CLASS_NAME, 'fa fa-2x fa-sign-in')
    #BUTTON = (By.CSS_SELECTOR, 'button[onclick="addElement()"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR,'button[class="radius"]')
    INVALID_MSG_TEXT = (By.CLASS_NAME,'flash error')
    WELLCOME_TEXT = (By.CLASS_NAME,'subheader')



    # URL
    URL = 'https://the-internet.herokuapp.com/secure'

    def __init__(self, browser):
        self.browser = browser

    def get_welcome_text(self, browser):
        return self.browser.find_element(*self.WELLCOME_TEXT).text