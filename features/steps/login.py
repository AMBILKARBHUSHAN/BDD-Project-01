from behave import *


@given(u'I navigated to login page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I navigated to login page')


@when(u'I entered the valid username and valid password into the fields')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I entered the valid username and valid password into the fields')


@when(u'I clicked on login button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I clicked on login button')


@then(u'I should get logged in')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should get logged in')


@when(u'I entered the invalid username and invalid password into the fields')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I entered the invalid username and invalid password into the fields')


@when(u'I entered the valid username and invalid password into the field')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I entered the valid username and invalid password into the field')


@then(u'Proper warning messages should be displayed')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Proper warning messages should be displayed')


@when(u'I entered the invalid username and valid password into the field')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I entered the invalid username and valid password into the field')


@when(u'I entered nothing into the username and password field')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I entered nothing into the username and password field')


@then(u'Proper warning message should be displayed')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Proper warning message should be displayed')
