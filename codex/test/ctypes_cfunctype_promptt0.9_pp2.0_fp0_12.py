import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

def callback(arg):
    print('callback', arg)

CALLBACK = ctypes.CFUNCTYPE(None, ctypes.py_object)

# Call a C callback
