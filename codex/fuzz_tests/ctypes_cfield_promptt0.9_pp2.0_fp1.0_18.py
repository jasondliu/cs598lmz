import ctypes
# Test ctypes.CField as an argument to struct.__setattr__ and ctypes.c_void_p.in_dll

if __name__ == "__main__":
    import os, sys, struct; from ctypes import *
    if sys.platform == 'win32':
        libname = 'msvcr80d.dll'
        clibname = 'msvcrt.dll'
    else:
        libname = 'libm.dylib'
        clibname = 'libc.so.6'
        
    mdll = CDLL(libname)
    
    class xdouble(Union):
        _fields_ = [
            ('x', c_double),
            ('hi', c_int),
            ('lo', c_int),
            ]

    class ystruct(Structure):
        _fields_ = [
            ('a', c_double),
            ('b', xdouble),
            ('c', c_double),
            ]

    class dstruct(Structure):
        _fields_ = [
            ('x', ystruct),
            ('y', ystruct),
           
