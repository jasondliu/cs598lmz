import ctypes
# Test ctypes.CField class
import pdb
#pdb.set_trace()
import string
#from LoadLibrary import *
import sys
import os
import logging
#lg = logging.getLogger("loadlib")

class CFieldEx(object):
    '''
    CFieldEx class is to convert DB value to the value
    of python data type, so that we can easily convert it 
    to data for Zabbix server.
    '''
    def __init__(self, fieldNo, name, baseTypeName):
        '''
        Constructor
        '''
        
        self.baseTypeName = baseTypeName
        self.fieldNo = fieldNo
        self.name = name
        self.baseType = None
        self.color = None
        #self.logger = logging.getLogger("loadlib")
#         try:
#             self.baseType = getBaseType(self.baseTypeName)
#         except KeyError, e:
#             #lg.error("Exception: {0!s}".format(e))
#             print "Exception: {0
