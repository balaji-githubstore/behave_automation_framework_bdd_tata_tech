from assertpy import assert_that
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@when(u'I click on patient menu')
def step_impl(context):
    # context.driver.find_element(By.XPATH, "//div[text()='Patient']").click()
    context.main_page.click_on_patient()


@when(u'I click on new-search menu')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//div[text()='New/Search']").click()


@when(u'I fill the add patient form')
def step_impl(context):
    context.driver.switch_to.frame(context.driver.find_element(By.XPATH, "//iframe[@name='pat']"))

    context.driver.find_element(By.CSS_SELECTOR, "#form_fname").send_keys(context.table[0]["firstname"])

    context.driver.find_element(By.CSS_SELECTOR, "#form_lname").send_keys(context.table[0]["lastname"])

    context.driver.find_element(By.XPATH, "//input[@id='form_DOB']").send_keys(context.table[0]["dob"])

    select_gender = Select(context.driver.find_element(By.XPATH, "//select[@id='form_sex']"))
    select_gender.select_by_visible_text(context.table[0]["gender"])

    if str(context.table[0]["licence_id"]) != 'NA':
        context.driver.find_element(By.XPATH, "//input[@id='form_drivers_license']").send_keys(
            context.table[0]["licence_id"])

    if str(context.table[0]["licence_id"]) != 'Yes':
        context.driver.find_element(By.XPATH, "//input[@id='form_drivers_license']").click()
    # else:
    #     context.driver.find_element(By.XPATH, "//input[@id='form_drivers_license']").click()


@when(u'I click on create new patient')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//button[@id='create']").click()
    context.driver.switch_to.default_content()


@when(u'I click on confirm create new patient')
def step_impl(context):
    context.driver.switch_to.frame(context.driver.find_element(By.XPATH, "//iframe[@id='modalframe']"))
    context.driver.find_element(By.XPATH, "// input[ @ value = 'Confirm Create New Patient']").click()
    context.driver.switch_to.default_content()


@when(u'I store the alert text and handle it')
def step_impl(context):
    wait = WebDriverWait(context.driver, 30)
    wait.until(expected_conditions.alert_is_present())

    context.actual_alert_text = context.driver.switch_to.alert.text
    context.driver.switch_to.alert.accept()


@when(u'I close hbd popup if available')
def step_impl(context):
    if len(context.driver.find_elements(By.XPATH, "//div[@class ='closeDlgIframe']")) > 0:
        context.driver.find_element(By.XPATH, "//div[@class ='closeDlgIframe']").click()


@then(u'I should get the added patient detail as "{expected_patient}"')
def step_impl(context, expected_patient):
    context.driver.switch_to.frame(context.driver.find_element(By.XPATH, "//iframe[@name='pat']"))
    actual_added_paitent = context.driver.find_element(By.XPATH,
                                                       "//h2[contains(text(),'Medical Record Dashboard')]").text
    assert_that(actual_added_paitent).contains(expected_patient)


@then(u'I should validate the alert text contains "{expected_alert_text}"')
def step_impl(context, expected_alert_text):
    assert_that(context.actual_alert_text).contains(expected_alert_text)
