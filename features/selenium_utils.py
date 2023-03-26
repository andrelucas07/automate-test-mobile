from time import sleep

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_for_find_element(driver, element, type_):
    find_element = None
    if type_ == 'xpath':
        find_element = WebDriverWait(driver, 90).until(
            EC.presence_of_element_located((AppiumBy.XPATH, element))
        )
    if type_ == 'class':
        find_element = WebDriverWait(driver, 90).until(
            EC.presence_of_element_located((AppiumBy.CLASS_NAME, element))
        )
    if type_ == 'text':
        find_element = WebDriverWait(driver, 90).until(
            EC.presence_of_element_located(
                (AppiumBy.ANDROID_UIAUTOMATOR, 'text("%s")' % element)
            )
        )
    return find_element


def click_element(driver, element, type_):
    wait_for_find_element(driver, element, type_).click()


def multiple_clicks(driver, element, type_, quantity):
    for i in range(quantity):
        sleep(1)
        click_element(driver, element, type_)
        i += 1


def send_keys(driver, content):
    ActionChains(driver).send_keys(content).perform()
