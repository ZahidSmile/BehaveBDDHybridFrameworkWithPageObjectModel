import pathlib
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from utilities import ConfigReader


def before_feature(context, feature):

    # Check if Chrome WebDriver exists
    try:
        # Reading Config Files & Getting Key & Value
        chrome_driver_path = ConfigReader.read_configuration("WebDriver", "chrome_path")

        # Initialize Chrome WebDriver
        context.driver = webdriver.Chrome(service=Service(chrome_driver_path))
    except FileNotFoundError:
        print("Chrome WebDriver not found. Please ensure the path is correct.")


def after_feature(context, feature):
    context.driver.close()