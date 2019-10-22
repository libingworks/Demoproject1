#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      suresh.kumar
#
# Created:     25-12-2017
# Copyright:   (c) suresh.kumar 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import os
import sys
import unittest
import datetime
#import HTMLTestRunner
import unittest
import shutil
import capture
#import HTMLTestRunnernew



#currentpath = os.path.dirname(os.path.realpath(__file__))
#print currentpathE:\Demoproject\Library\HTMLTestRunner.py
#folderpath = os.path.abspath(os.path.join(currentpath,os.pardir))
#print folderpath
folderpath = os.path.realpath('E:\Demoproject')
#print folderpath

sys.path.append(folderpath+'\Testscripts')
sys.path.append(folderpath+'\Library')

#sys.path.insert(0,folderpath+'\Testscripts')
#sys.path.insert(0,folderpath+'\Library')

from Launchapplication import launchapplication
from ApplicationSignIn import applicationsignin
import HTMLTestRunner
#import HTMLTestRunnernew


suite = unittest.TestSuite()

suite.addTest(launchapplication('test_launchapplication'))
#suite.addTest(applicationsignin('test_applicationsignin'))


todaysdate = datetime.datetime.today().strftime('%d_%m_%Y-%H_%M_%S')

outfile = file(folderpath+'\TestReport\Regressionreport-%s.html' %todaysdate,'w')


#runner = HTMLTestRunner.HTMLTestRunner(stream = outfile,verbosity = 2,title='Regression Report', description='Automation report')
runner = HTMLTestRunner.HTMLTestRunner(stream = outfile,verbosity = 2,title='Regression Report', description='Automation report',dirTestScreenshots=folderpath+'\Screenshots')

runner.run(suite)

outfile.close()











