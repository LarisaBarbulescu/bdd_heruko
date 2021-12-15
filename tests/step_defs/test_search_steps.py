from time import sleep
from pytest_bdd import scenarios, when, then, given, parsers
from pages.login_page import LoginPage
from pages.secure_page import SecurePage

#Scenario
scenarios('../features/heruko.feature')
# Shared Given Steps
@given('open the login page')
def open_page(browser):
    login_page = LoginPage(browser)
    login_page.loadPage()

@when(parsers.cfparse('user type username "{username}"'))
def input_username(browser, username):
    login_page = LoginPage(browser)
    login_page.insertUsernameField(username)

@when(parsers.cfparse('user type password "{password}"'))
def input_password(browser, password):
    login_page = LoginPage(browser)
    login_page.insertPasswordField(password)

@when('user click login button')
def click_login(browser):
    login_page = LoginPage(browser)
    login_page.clickLoginButton()

@then('user has successfully logged in')
def check_welcome_text(browser):
    secure_page= SecurePage(browser)
    assert secure_page.get_welcome_text(browser) == 'Welcome to the Secure Area. When you are done click logout below.'




