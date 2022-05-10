import ctypes
# Test ctypes.CFUNCTYPE

from ctypes import *

def test1():
    import _ctypes_test
    dll = CDLL(_ctypes_test.__file__)
    CFUNCTYPE(c_int, c_int, c_int)(('testfunc', dll))(4, 5)
    CFUNCTYPE(c_int, c_int, c_int)(dll.testfunc)(4, 5)

def test2():
    from ctypes import util
    dll = CDLL(util.find_library("c"))
    atoi = CFUNCTYPE(c_int, c_char_p)(("atoi", dll))
    atoi("42")

def test3():
    from ctypes import util
    dll = CDLL(util.find_library("c"))
    atoi = CFUNCTYPE(c_int, c_char_p)(("atoi", dll))
    atoi("42")
    Int = c_int.in_dll(dll, "atoi")
    Int.value = 42
    at
