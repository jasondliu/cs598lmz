import ctypes
# Test ctypes.CFUNCTYPE(None)

import _ctypes_test

def callback():
    print("callback")

CALLBACK = ctypes.CFUNCTYPE(None)

_ctypes_test.set_callback(CALLBACK(callback))
# Test ctypes.CFUNCTYPE(None, ctypes.py_object)

import _ctypes_test

def callback(arg):
    print("callback", arg)

CALLBACK = ctypes.CFUNCTYPE(None, ctypes.py_object)

_ctypes_test.set_callback(CALLBACK(callback))
_ctypes_test.call_callback(b"hello")
# Test ctypes.CFUNCTYPE(None, ctypes.py_object, ctypes.py_object)

import _ctypes_test

def callback(arg1, arg2):
    print("callback", arg1, arg2)

CALLBACK = ctypes.CFUNCTYPE(None, ctypes.py_object, ctypes.py_object)

_ctypes_test
