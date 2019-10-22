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
import pdb
import os
import sys
import unittest
import datetime
import time
import traceback
from selenium import webdriver
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common import exceptions

folderpath = os.path.realpath('E:\Demoproject')
#print folderpath

sys.path.append(folderpath+'\Envsetup')
sys.path.append(folderpath+'\Library')

from browserSetup import launchbrowserclass
from launchwebsite import Launchwebsite
from datadriver import readxml

Datadriver = readxml()

browserlaunch = launchbrowserclass()

websitelaunch = Launchwebsite()

#wait = browser.implicitly_wait(10)



class applicationsignin(unittest.TestCase):
    def test_applicationsignin(self):
        try:

            browser = browserlaunch.Launchbrowser() # to open browser
            browser.implicitly_wait(10)
            #time.sleep(50)
            websitelaunch.launchWebsite(browser)# input url
            websitelaunch.appsign(browser) # click SignIn link
            time.sleep(1)
            browser.find_element_by_xpath("//input[@id='email_create']").send_keys('suresh4978@gmail.com')
            time.sleep(1)
            browser.find_element_by_xpath("//button[@id='SubmitCreate']").click()
            time.sleep(1)
            browser.find_element_by_xpath("//select[@id='days']").click()
            time.sleep(2)

            from random import randrange

            irand = randrange(1, 31)
            irand1 =  str(irand)
            date = irand1
            objectdate = Datadriver.xmlread(folderpath+'\Objects\Objects.xml','automation','Date')
            #objectdate = readxml.xmlread(folderpath+'\Objects\Objects.xml','automation','Date')

            parenthesis = "'{}'"
            date1 = parenthesis.format(date)
            kumar = '//option[@value=%s]'  %date1
            #kumar = objectdate
            time.sleep(2)
            dateselect  =  browser.find_element_by_xpath(kumar)
            time.sleep(1)
            dateselect.click()




##            authenticate_object = Datadriver.xmlread(folderpath+'\Objects\Objects.xml','automation','authenticate')
##            authenticate = browser.find_element_by_xpath(authenticate_object)
##            text1 =  authenticate.text
##            print text1
##            self.assertEqual(text1.lower(),'authentication')
        except Exception:

            #tc = 'applicationsignin'
            tf = 'test_applicationsignin'
            #imgpath = os.path.join(imgdir, "%s-%s.png"%(tc, tf))
            browser.get_screenshot_as_file(folderpath+'\Screenshots\Testcase-%s.png' %(tf))
            #todaysdate = datetime.datetime.today().strftime('%d-%M-%Y-%H-%M-%S')
            #browser.get_screenshot_as_file(folderpath+'\Screenshots\Testcase-%s.png' %todaysdate)
            #browser.get_screenshot_as_file(folderpath+'\Screenshots\Testcase002.png')
            traceback.print_exc()
            self.fail("Testcase002 is failed")
        #finally:
            #browserlaunch.closebrowser(browser)

    #def test_

if __name__ == '__main__':
    unittest.main()



