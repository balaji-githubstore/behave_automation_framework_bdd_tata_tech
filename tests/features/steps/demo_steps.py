from assertpy import assert_that
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@given(u'I have browser with openemr application')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(20)
    context.driver.get("https://demo.openemr.io/b/openemr")


@when(u'I enter username as "{text}"')
def step_impl(context, text):
    context.driver.find_element(By.ID, "authUser").send_keys(text)


@when(u'I enter password as "{text}"')
def step_impl(context, text):
    context.driver.find_element(By.ID, "clearPass").send_keys(text)


@when(u'I select language as "{text}"')
def step_impl(context, text):
    select_lan = Select(context.driver.find_element(By.XPATH, "//select[@name='languageChoice']"))
    select_lan.select_by_visible_text(text)


@when(u'I click on login')
def step_impl(context):
    context.driver.find_element(By.ID, "login-button").click()


@then(u'I should get access to the portal with title as "{text}"')
def step_impl(context, text):
    assert_that(text).is_equal_to(context.driver.title)
