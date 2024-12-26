Feature: Login functionality

  Scenario: login with valid credentials
    Given I navigated to login page
    When I entered the valid username and valid password into the fields
    And I clicked on login button
    Then I should get logged in

  Scenario: login with invalid credentials
    Given I navigated to login page
    When I entered the invalid username and invalid password into the fields
    And I clicked on login button
    Then I should get logged in

  Scenario: login with valid username and invalid password
    Given I navigated to login page
    When I entered the valid username and invalid password into the field
    And I clicked on login button
    Then Proper warning messages should be displayed

  Scenario: login with invalid username and valid password
    Given I navigated to login page
    When I entered the invalid username and valid password into the field
    And I clicked on login button
    Then Proper warning messages should be displayed

  Scenario: login without any credentials
    Given I navigated to login page
    When I entered nothing into the username and password field
    And I clicked on login button
    Then Proper warning message should be displayed

