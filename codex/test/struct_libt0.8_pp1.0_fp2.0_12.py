import _struct
#from ctypes import *

'''
parser for binary file
'''

class bfp:
    def __init__(self):
        self.file = ""
        self.start = 0
        self.end = 0

    def getfile(self, filename):
        self.file = filename
        return 0
