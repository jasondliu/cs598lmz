import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int)

C_cdecl_func = ctypes.cdll.lib.c_cdecl_func
print("C_cdecl_func result:  {}".format(C_cdecl_func()))

callback = FUNTYPE(fn)
C_cdecl_func.restype = ctypes.c_int
print("C_cdecl_func result:  {}".format(C_cdecl_func(2, 3)))
# C_cdecl_func result:  11
# C_cdecl_func result:  5


from math import sqrt

from ctypes import cdll, c_double, POINTER, byref
from ctypes.util import find_library
from ctypes import windll
from ctypes.wintypes import WINFUNCTYPE, BOOL, HWND, LPARAM

def g_wrap(*args):
    f = dll.g(*args)
    if f == 0:
        raise ZeroDivisionError
    return f
    

def f_wrap(*args):
    f = dll.f(*
