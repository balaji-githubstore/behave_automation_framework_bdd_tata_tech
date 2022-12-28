@login
Feature: Login
  In order to maintain the patient, doctors records
  As a user
  I want to access the OpenEMR dashboard

  Background:
    Given I have browser with openemr application

  @valid @smoke
  Scenario Outline: Valid Login
    When I enter username as "<username>"
    And I enter password as "<password>"
    And I select language as "<language>"
    And I click on login
    Then I should get access to the portal with title as "<expected_title>"
    Examples:
      | username   | password   | language         | expected_title |
      | physician  | physician  | English (Indian) | OpenEMR        |
#      | admin      | pass       | English (Indian) | OpenEMR        |
#      | accountant | accountant | English (Indian) | OpenEMR        |

  @invalid
  Scenario: Invalid Login
    When I enter username as "john"
    And I enter password as "john123"
    And I select language as "English (Indian)"
    And I click on login
    Then I should not get access to portal with error as "Invalid username or password"

