#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      suresh.kumar
#
# Created:     17-12-2017
# Copyright:   (c) suresh.kumar 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import xml.etree.ElementTree as ET

##class readxml():
##    def xmlread(self,filename,rootnode,finalnode):
##        filename = ET.parse(filename)
##        root = filename.getroot()
##        for root1 in root.findall(rootnode):
##            value = root1.find(finalnode).text
##            return value



#filename = ET.parse("E:\Demoproject\Envsetup\setup.xml") # file
filename = ET.parse("E:\Demoproject1\Env\envsetup.xml") # file
print filename
root = filename.getroot() # mainroot
print root
for root1 in root.findall("setup"): #rootnode
    print root1
    value = root1.find("browser").text #final node
    print value
    #return value



