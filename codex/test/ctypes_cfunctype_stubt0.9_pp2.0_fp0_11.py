import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return u'\xe2\x9c\xbee'

# This should raise an error during setup
