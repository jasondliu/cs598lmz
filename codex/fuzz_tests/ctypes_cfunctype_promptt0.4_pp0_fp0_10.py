import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# simple function call

func = lib.my_function
func.argtypes = (ctypes.c_int, ctypes.c_int)
func.restype = ctypes.c_int

func(1, 2)

# call a function with a structure argument

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_char * 3)]

func = lib.my_function_s
func.argtypes = (X,)
func.restype = ctypes.c_int

func(X(1, b"abc"))

# call a function with a structure argument, with the structure
# defined in C

class Y(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_char * 3)]

func = lib.my_function_s2
func.
