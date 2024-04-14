from behave import given, when, then
from pages.orangehrm_page import OrangehrmPage


@given('Opening the OrangeHRM URL')
def step_impl(context):
    context.driver = OrangehrmPage(context.driver)
    context.driver.open()


@when('I entered the username and password')
def step_impl(context):
    context.driver.credentials()


@then('I should see the dashboard')
def step_impl(context):
    context.driver.result()