#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      suresh.kumar
#
# Created:     27-03-2018
# Copyright:   (c) suresh.kumar 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import os
import sys
import time


folderpath = os.path.abspath('E:\Demoproject')
print folderpath

foldername = os.path.basename(folderpath)
print foldername

sys.path.append(folderpath+'\Envsetup')
sys.path.append(folderpath+'\Library')
sys.path.append(folderpath+'\Syslibrary')

from random import randrange

#from datadriver import readxml

#Datadriver = readxml()


irand = randrange(1900, 2018)
irand1 =  irand

#date = irand1 + '/' + 'Jan' + '/' + str(1982)
date = irand1

#print date

#suresh = date

parenthesis = "'{}'"
date1 = parenthesis.format(date)
#print date1

#print suresh
kumar = '//option[@value= %s]' % date1
#//option[@value='11']
print kumar

print "My name is %s and weight is %d kg!" % ('Zara', 21)


##objectdate = Datadriver.xmlread(folderpath+'\Objects\Objects.xml','automation','Date')
##time.sleep(3)
##print date1
##test = objectdate
##print test
##print date
##print date1
##print date
#suresh = format(date)
#print Date_object
#Date = browser.find_element_by_xpath(Date_object)
#text1 =  date

#print suresh

##email1 = '9/Jan/1982'
##parenthesis = "'{}'"
##user1 = parenthesis.format(email1)
##print user1



