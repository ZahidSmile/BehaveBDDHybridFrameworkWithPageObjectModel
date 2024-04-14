Feature: Google Search

  Scenario: Searching on Google
    Given I am on the Google homepage
    When I search for "Selenium"
    Then I should see search results