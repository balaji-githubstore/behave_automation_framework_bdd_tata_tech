@patient
Feature: Patient
  In order to manage the patient details
  As an admin
  I would like to add, edit, delete the patient records

  @addpatient
  Scenario: Add Valid Patient
    Given I have browser with openemr application
    When I enter username as "admin"
    And I enter password as "pass"
    And I select language as "English (Indian)"
    And I click on login
    And I click on patient menu
    And I click on new-search menu
    And I fill the add patient form
      | firstname | lastname | dob        | gender |
      | John      | Wick     | 2022-12-27 | Female |
    And I click on create new patient
    And I click on confirm create new patient
    And I store the alert text and handle it
    And I close hbd popup if available
    Then I should get the added patient detail as "Medical Record Dashboard - John Wick"
    And I should validate the alert text contains "Tobacco"



