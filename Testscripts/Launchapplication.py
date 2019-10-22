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
import unittest
import datetime
import traceback
from selenium.webdriver.support import expected_conditions as EC
#from selenium.common.exceptions import NoSuchElementException

folderpath = os.path.realpath('E:\Demoproject')
#print folderpath
sys.path.append(folderpath+'\Envsetup')
sys.path.append(folderpath+'\Library')

from browserSetup import launchbrowserclass
from launchwebsite import Launchwebsite

browserlaunch = launchbrowserclass()

websitelaunch = Launchwebsite()



class launchapplication(unittest.TestCase):
    def test_launchapplication(self):
        try:

            browser = browserlaunch.Launchbrowser() # to open browser
            websitelaunch.launchWebsite(browser)# input url
            print browser.title
            self.assertEqual(browser.title,'My Store1')
        except Exception:
            #print launchapplication().__class__.__name__

            #x = str(test).split()
            #tc = 'launchapplication'
            tf = 'test_launchapplication'
            #imgpath = os.path.join(imgdir, "%s-%s.png"%(tc, tf))
            browser.get_screenshot_as_file(folderpath+'\Screenshots\Testcase-%s.png' %(tf))
            #todaysdate = datetime.datetime.today().strftime('%d-%M-%Y-%H-%M-%S')
            #browser.get_screenshot_as_file(folderpath+'\Screenshots\Testcase-%s.png' %todaysdate)
            #browser.get_screenshot_as_file(folderpath+'\Screenshots\Testcase001.png')
            traceback.print_exc()
            self.fail("Testcase001 is failed")
        finally:
            browserlaunch.closebrowser(browser)

#if __name__ == '__main__':
    #unittest.main()



