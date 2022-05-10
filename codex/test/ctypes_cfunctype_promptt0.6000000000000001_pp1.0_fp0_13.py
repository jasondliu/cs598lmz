import ctypes
# Test ctypes.CFUNCTYPE
import _testcapi

def PyCFuncPtr_Check(obj):
    if not isinstance(obj, ctypes.CFUNCTYPE):
        return 0
    return 1

def PyCFuncPtr_CheckExact(obj):
    if not type(obj) is ctypes.CFUNCTYPE:
        return 0
    return 1

