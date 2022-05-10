import ctypes

class S(ctypes.Structure):
    x = ctypes.c_float()
    y = ctypes.c_float()

__doc__ = """
>>> from ctypes import *
>>> cdll.msvcrt.malloc(10)
0
>>> cdll.msvcrt.free(0)

>>> from ctypes import *
>>> cdll.msvcrt.malloc.restype = c_void_p
>>> cdll.msvcrt.malloc(10)
0
>>> cdll.msvcrt.free(0)

>>> from ctypes import *
>>> cdll.msvcrt.malloc(10)
Exception: Procedure called with not enough arguments (10 bytes missing) or wrong calling convention
>>> cdll.msvcrt.malloc(10, alignment=1)
0
>>> cdll.msvcrt.free(0)

>>> from ctypes import *
>>> cdll.msvcrt.malloc.restype = c_void_p
>>> cdll.msvcrt.malloc(10)
Exception: Procedure called with not enough arguments (10 bytes
