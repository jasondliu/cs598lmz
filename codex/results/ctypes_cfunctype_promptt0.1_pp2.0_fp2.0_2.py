import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a function pointer argument
# this function is declared as:
# void func(void (*callback)())

CALLBACK = ctypes.CFUNCTYPE(None)

def callback():
    print "callback called"

func = lib.func
func.argtypes = CALLBACK,
func.restype = None

func(CALLBACK(callback))

# call a function with a function pointer argument
# this function is declared as:
# void func2(void (*callback)(int), int arg)

CALLBACK2 = ctypes.CFUNCTYPE(None, ctypes.c_int)

def callback2(arg):
    print "callback2 called with", arg

func2 = lib.func2
func2.argtypes = CALLBACK2, ctypes.c_int
func2.restype = None

func2(CALLBACK2(callback2), 42)

# call a function with a function pointer argument
