import ctypes
ctypes.cast(0, ctypes.py_object)

# SOURCE LINE 4

import sys

def _mimport(name, level=1):
    try:
        return __import__(name, globals(), level=level)
    except:
        return __import__(name, globals())

_data=_mimport('mdsdata')
_compound=_mimport('mdsarray')
_mdsshr=_mimport('_mdsshr')

class MdsException(Exception):
    status=None
    message=None
    def __init__(self,status):
        self.status=status
        self.message=_mdsshr.MdsGetMsg(status)
    def __str__(self):
        return self.message

class TdiException(MdsException):
    def __init__(self,status):
        self.status=status
        self.message=_mdsshr.MdsGetMsg(status)
        self.message=self.message[self.message.find('\n')+1:]

class TreeException(
