import os
import time
import logging

from time import strftime
from selenium import webdriver
from msedge.selenium_tools import Edge,EdgeOptions
from selenium.webdriver.edge.options import Options

from input.config import PARAMETERS_INPUT


### Kill Process ###
try:
    os.system("taskkill /im msedge.exe /f")
    time.sleep(4)
except ValueError:
    pass

### Open WebDriver ###
def start_webdriver():
    option = EdgeOptions()
    # layout options
    option.add_argument("--start-maximized")
    option.add_argument("--disable-infobars")
    # security options
    option.add_argument("--inprivate")
    option.add_argument('--disable-geolocation')
    option.add_argument('--disable-web-security')
    option.add_argument("--disable-extensions")
    option.add_argument('--ignore-certificate-errors')
    option.add_experimental_option('useAutomationExtension', False)
    option.add_experimental_option('excludeSwitches', ['enable-popup-blocking'])
    # Pass the argument 1 to allow and 2 to block
    option.add_experimental_option("prefs", {
        "profile.default_content_setting_values.notifications": 1
    })
    option.add_experimental_option("detach", True)
    browser = webdriver.Edge(PARAMETERS_INPUT['path_driver'])
    return browser


def screenshot(passo, driver, path):
    name = path+"\error_"+passo+str(strftime('%Y%m%d%H%M'))+str(".png")
    driver.get_screenshot_as_file(filename=name)
    return


# def start_logging(processo, dev, modification, log_path):
#     log_path+"\log_"+str(strftime('%d-%m-%Y'))
#     logging.basicConfig(
#         filename= log_path+"\log_"+str(strftime('%d-%m-%Y')),
#         level=logging.INFO,
#         format='[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
#         datefmt='%H:%M:%S'
#     )
#     logging.info(processo)
#     logging.info(dev)
#     logging.info(modification)
#     logging.info('----------------------------------')
#     logging.info('----------------------------------')


def finish_drive(driver):
    driver.close()
    os.system("taskkill /im msedge.exe /f")
