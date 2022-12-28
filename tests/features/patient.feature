@patient
Feature: Patient
  In order to manage the patient details
  As an admin
  I would like to add, edit, delete the patient records


  @addpatient
  Scenario Outline: Add Valid Patient
    Given I have browser with openemr application
    When I enter username as "<username>"
    And I enter password as "<password>"
    And I select language as "<language>"
    And I click on login
    And I click on patient menu
    And I click on new-search menu
    And I fill the add patient form
      | firstname | lastname | dob   | gender   | licence_id   |
      | <fname>   | <lname>  | <dob> | <gender> | <licence_id> |
    And I click on create new patient
    And I click on confirm create new patient
    And I store the alert text and handle it
    And I close hbd popup if available
    Then I should get the added patient detail as "<expected_patient_record>"
    And I should validate the alert text contains "<expected_alert>"
    Examples:
      | username | password | language         | fname | lname | licence_id | dob        | gender | expected_patient_record              | expected_alert |
      | admin    | pass     | English (Indian) | John  | Wick  | Yes        | 2022-12-27 | Female | Medical Record Dashboard - John Wick | Tobacco        |
#      | admin    | pass     | English (Indian) | Jack  | Ken   | 8788dfs    | 2022-12-28 | Male   | Medical Record Dashboard - Jack Ken  | Tobacco        |


#  @addpatient
#  Scenario: Add Valid Patient
#    Given I have browser with openemr application
#    When I enter username as "admin"
#    And I enter password as "pass"
#    And I select language as "English (Indian)"
#    And I click on login
#    And I click on patient menu
#    And I click on new-search menu
#    And I fill the add patient form
#      | firstname | lastname | dob        | gender |
#      | John      | Wick     | 2022-12-27 | Female |
#    And I click on create new patient
#    And I click on confirm create new patient
#    And I store the alert text and handle it
#    And I close hbd popup if available
#    Then I should get the added patient detail as "Medical Record Dashboard - John Wick"
#    And I should validate the alert text contains "Tobacco"
#
#
#  @addpatient
#  Scenario: Add Valid Patient
#    Given I have browser with openemr application
#    When I enter username as "admin"
#    And I enter password as "pass"
#    And I select language as "English (Indian)"
#    And I click on login
#    And I click on patient menu
#    And I click on new-search menu
#    And I fill the add patient form
#      | firstname | lastname | dob        | gender |
#      | Jack      | Ken      | 2022-12-28 | Male   |
#    And I click on create new patient
#    And I click on confirm create new patient
#    And I store the alert text and handle it
#    And I close hbd popup if available
#    Then I should get the added patient detail as "Medical Record Dashboard - John Wick"
#    And I should validate the alert text contains "Tobacco"
