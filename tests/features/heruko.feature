Feature: Heruko Login Browsing
    Login on the page

    Scenario: herukoLoginSucceed
      Given login: user is on the login page
      When login: user enters valid username "email" and valid password "pass"
      Then login: verify that the login succeed


    Examples:
      | email                   | pass      |
      | tomsmith                | SuperSecretPassword! |
      | itfactory2.ro@gmail.com | password2 |
      | itfactory3.ro@gmail.com | password3 |
