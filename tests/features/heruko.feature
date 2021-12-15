Feature: Heruko Login Browsing
    Login on the page

    Scenario: herukoLoginSucceed
      Given open the login page
      When user type username "tomsmith"
      And user type password "SuperSecretPassword!"
      And user click login button
      Then user has successfully logged in
