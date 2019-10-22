#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      suresh.kumar
#
# Created:     17-12-2017
# Copyright:   (c) suresh.kumar 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import unittest

import os
import sys

##currentpath = os.path.dirname(os.path.realpath(__file__))
##print currentpath
##folderpath = os.path.abspath(os.path.join(currentpath,os.pardir))
##print folderpath

folderpath = os.path.realpath('E:\Demoproject')
#print folderpath

sys.path.append(folderpath+'\Syslibrary')

##folderpath = os.path.realpath('\Demoproject\Syslibrary')
##sys.path.insert(0,folderpath+'\Syslibrary')
###print folderpath



from datadriver import readxml


Datadriver = readxml()

class launchbrowserclass():
    def Launchbrowser(self):
        env = Datadriver.xmlread(folderpath+'\Envsetup\setup.xml','setup','browser')
        print env
        if env == 'firefox':
            #browser = webdriver.Firefox("C:\Users\suresh.kumar\Downloads\geckodriver-v0.19.1-win64\geckodriver.exe")
            browser = webdriver.Firefox()
            #browser.implicitly_wait(10)
            browser.maximize_window()

            return browser

        elif env == 'chrome':
            browser = webdriver.Chrome("C:\Users\suresh.kumar\Downloads\chromedriver.exe")
            browser.maximize_window()
            return browser
    def closebrowser(self,browser):
            browser.close()

#if __name__ == '__main__':
    #unittest.main()


#class Browserlaunch():
    #def browserlaunch(self):




