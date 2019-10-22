#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      suresh.kumar
#
# Created:     30-12-2017
# Copyright:   (c) suresh.kumar 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common import exceptions
import time

browser = webdriver.Firefox()
browser.implicitly_wait(10)
browser.maximize_window()


browser.get('https://onlinebanking.nationwide.co.uk/AccessManagement/Login')

memorydata = browser.find_element_by_xpath("//span[text()='Log in using my memorable data']")

#memorydata = browser.find_element_by_xpath("//label[@class='choice-list__option__description']//span[text()='Log in using my memorable data']")


print memorydata

assert memorydata.text == 'Log in using my memorable data'

memorydata.click()

#login = []

login = browser.find_element_by_xpath("//button[@class='action__button']")

browser.execute_script("arguments[0].scrollIntoView(true);", login)

#time.sleep(3)

login.click()

dropdown =[]

dropdown = browser.find_elements_by_xpath("//div[@class='selection-list selection-list--secret selection-list--disabled']")

dropdown[0].click()




