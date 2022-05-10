import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double)

import os
import numpy as np

def get_library_path():
    current_path = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(current_path, "libcpp_fun.so")

class Fun:
    def __init__(self):
        path = get_library_path()
        self.lib = ctypes.cdll.LoadLibrary(path)

        self.lib.fun.restype = ctypes.c_double
        self.lib.fun.argtypes = [ctypes.c_double, ctypes.c_double]

    def __call__(self, x, y):
        return self.lib.fun(x, y)

class Integrator:
    def __init__(self):
        path = get_library_path()
        self.lib = ctypes.cdll.LoadLibrary(path)

        self.lib.integrate_fun.restype = ctypes.c
