import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

#
# The following functions are declared in _ctypes_test.h:
#
# int func(int)
# int func_p(int *p)
# int func_pp(int **pp)
# int func_ppp(int ***ppp)
#

func = lib.func
func.restype = ctypes.c_int
func.argtypes = (ctypes.c_int,)

func_p = lib.func_p
func_p.restype = ctypes.c_int
func_p.argtypes = (ctypes.POINTER(ctypes.c_int),)

func_pp = lib.func_pp
func_pp.restype = ctypes.c_int
func_pp.argtypes = (ctypes.POINTER(ctypes.POINTER(ctypes.c_int)),)

func_ppp = lib.func_ppp
func_ppp.restype = ctypes.c_int
