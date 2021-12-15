from time import sleep
from pytest_bdd import scenarios, when, then, given, parsers
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Constants
HERUKO_LOGIN = 'https://the-internet.herokuapp.com/login'
# Scenarios
scenarios('../features/heruko.feature')
# Shared Given Steps
@given('login: user is on the login page')
def hrk_login(browser):
    browser.get(HERUKO_LOGIN)
@when('login: user enters valid username "email" and valid password "pass"')
def step_impl(browser, username, password):
    browser.login_page.login(username, password)
@then('login: verify that the login succeed')
def step_impl(browser):
    #browser.login_page.verify_error_displayed()
    invalid_login = browser.find_elements(By.XPATH,"//*[@class='flash error']")
    assert len(invalid_login) == 0
