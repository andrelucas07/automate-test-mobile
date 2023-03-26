from appium import webdriver
from behave import *


@fixture
def before_scenario(context, scenario):
    desired_capabilities = {
        "platformName": 'Android',
        "deviceName": 'emulator-5554',
        "appPackage": 'br.com.napista',
        "appActivity": "br.com.simplificauto.napista.MainActivity",
        "autoGrantPermissions": True,
        "ensureWebviewsHavePages": True,
        "nativeWebScreenshot": True,
        "newCommandTimeout": 3600,
        "connectHardwareKeyboard": True,
        "unicodeKeyboard": True,
        "resetKeyboard": True,
    }

    context.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities)


def after_scenario(context, scenario):
    context.driver.quit()
