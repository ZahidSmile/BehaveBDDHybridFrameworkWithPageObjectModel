from behave import given, when, then
from pages.google_page import GoogleSearchPage


@given('I am on the Google homepage')
def step_impl(context):
    context.driver = GoogleSearchPage(context.driver)
    context.driver.goto_google()


@when('I search for "{keyword}"')
def step_impl(context, keyword):
    context.driver.search(keyword)


@then('I should see search results')
def step_impl(context):
    context.driver.is_search_results_present()
