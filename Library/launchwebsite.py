#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      suresh.kumar
#
# Created:     23-12-2017
# Copyright:   (c) suresh.kumar 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os
import sys
import time
#from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

folderpath = os.path.realpath('E:\Demoproject')
print folderpath

sys.path.append(folderpath+'\Syslibrary')


from datadriver import readxml

Datadriver = readxml()




class Launchwebsite():
    def launchWebsite(self,browser):
        url = Datadriver.xmlread(folderpath+'\Data\data.xml','automation','url')
        browser.get(url)

    def appsign(self,browser):
        browser.implicitly_wait(10)
        signin_object = Datadriver.xmlread(folderpath+'\Objects\Objects.xml','automation','signIn')
        signin = browser.find_element_by_xpath(signin_object)
        signin.click()





