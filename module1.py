#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      suresh.kumar
#
# Created:     06-03-2018
# Copyright:   (c) suresh.kumar 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

##import time
##
##from selenium import webdriver
##browser = webdriver.Chrome('C:\Selenium\chromedriver.exe')
##
##browser.get('http://google.co.in')
##
##time.sleep(2)
##
##imgpath = 'E:/Demoproject/Screenshots/test.png'
##
##browser.get_screenshot_as_file(imgpath)
##browser.save_screenshot
##
##browser.close()



#instance.__class__.__name__

#example:
import unittest

##class A(unittest.TestCase):
##    pass
###a = A(unittest.TestCase)
###print a.__class__.__name__
##print A(unittest.TestCase).__class__.__name__
###'A'



class A(unittest.TestCase):
#class A():
  #pass
 b = unittest.TestCase.shortDescription()
#print A(unittest.TestCase).__name__
 print b

 #a = unittest.TestCase.shortDescription(b)
 #print a


##class aclass(unittest.TestCase):
## pass
##a = aclass(unittest.TestCase)
##type(a)
###<class '__main__.aclass'>
##a.__class__
###<class '__main__.aclass'>
##
##print type(a).__name__
###'aclass'
##
##print a.__class__.__name__
###'aclass'







