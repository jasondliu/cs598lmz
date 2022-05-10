import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double,ctypes.c_double,ctypes.c_double,ctypes.c_double,ctypes.c_double,ctypes.c_double,ctypes.c_double,ctypes.c_double,ctypes.c_double,ctypes.c_double,ctypes.c_double)

import numpy as np

def get_f_from_dll(dll_path,func_name):
    dll = ctypes.CDLL(dll_path)
    return FUNTYPE(dll[func_name])


def get_f_from_so(so_path,func_name):
    so = ctypes.CDLL(so_path)
    return FUNTYPE(so[func_name])

def get_f_from_wll(wll_path,func_name):
    wll = ctypes.WinDLL(wll_path)
    return FUNTYPE(wll[func_name])

def get_f_from_pyd(pyd_path,func_name):
    pyd = ctypes.
