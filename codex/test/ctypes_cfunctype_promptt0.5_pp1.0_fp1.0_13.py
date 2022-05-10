import ctypes
# Test ctypes.CFUNCTYPE(None)

import _ctypes_test

def callback():
    print("callback")

CALLBACK = ctypes.CFUNCTYPE(None)

