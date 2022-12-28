from assertpy import assert_that
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from tests.features.steps.environment import init_page_objects


@given(u'I have browser with openemr application')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(20)
    context.driver.get("https://demo.openemr.io/b/openemr")
    init_page_objects(context)


@when(u'I enter username as "{text}"')
def step_impl(context, text):
    # context.driver.find_element(By.ID, "authUser").send_keys(text)
    context.login_page.enter_username(text)


@when(u'I enter password as "{text}"')
def step_impl(context, text):
    # context.driver.find_element(By.ID, "clearPass").send_keys(text)
    context.login_page.enter_password(text)


@when(u'I select language as "{text}"')
def step_impl(context, text):
    select_lan = Select(context.driver.find_element(By.XPATH, "//select[@name='languageChoice']"))
    select_lan.select_by_visible_text(text)


@when(u'I click on login')
def step_impl(context):
    context.login_page.click_login()


@then(u'I should get access to the portal with title as "{text}"')
def step_impl(context, text):
    assert_that(text).is_equal_to(context.driver.title)


@then(u'I should not get access to portal with error as "{text}"')
def step_impl(context, text):
    actual_error = context.driver.find_element(By.XPATH, "// *[contains(text(), 'Invalid')]").text
    assert_that(actual_error).contains(text)
