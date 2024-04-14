Feature: OrangeHRM Login

  Scenario: Login on OrangeHRM
    Given Opening the OrangeHRM URL
    When I entered the username and password
    Then I should see the dashboard
