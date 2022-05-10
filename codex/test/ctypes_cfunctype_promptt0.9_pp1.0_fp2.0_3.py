import ctypes
# Test ctypes.CFUNCTYPE() with Python object as input arg and
# return type.

import _ctypes_test

class PythonObj(object):
    def __init__(self, val):
        self.val = val
    def __repr__(self):
        return "<value=%s>" % self.val

ReprFunc = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object)

