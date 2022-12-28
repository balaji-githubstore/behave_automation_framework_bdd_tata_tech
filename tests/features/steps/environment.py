from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.patient_dashboard_page import PatientDashboardPage
from pages.search_or_add_patient_page import SearchOrAddPatientPage


def init_page_objects(context):
    context.login_page = LoginPage(context.driver)
    context.main_page = MainPage(context.driver)
    context.patient_page = PatientDashboardPage(context.driver)
    context.search_add_page = SearchOrAddPatientPage(context.driver)


def after_scenario(context, scenario):
    context.driver.quit()
