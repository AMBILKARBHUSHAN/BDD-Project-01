from selenium import webdriver
from utilities import ConfigReader


def before_scenario(context, driver):
    browser_name = ConfigReader.read_configuration("basic info", "browser")
    if browser_name.__eq__("chrome"):
        context.driver = webdriver.Chrome()
    elif browser_name.__eq__("edge"):
        context.driver = webdriver.Edge()
    elif browser_name.__eq__("firefox"):
        context.driver = webdriver.Firefox()
    else:
        context.driver = webdriver.Chrome()

    context.driver.maximize_window()
    context.driver.get(ConfigReader.read_configuration("basic info", "url"))


def after_scenario(context, driver):
    context.driver.quit()
