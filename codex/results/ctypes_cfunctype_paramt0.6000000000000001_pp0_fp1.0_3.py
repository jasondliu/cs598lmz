import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double)

def get_fun(name):
    return FUNTYPE(getattr(lib, name))

def get_fun_x(name):
    return FUNTYPE(getattr(lib, name + '_x'))

def get_fun_xy(name):
    return FUNTYPE(getattr(lib, name + '_xy'))

def get_fun_xz(name):
    return FUNTYPE(getattr(lib, name + '_xz'))

def get_fun_yz(name):
    return FUNTYPE(getattr(lib, name + '_yz'))

def get_fun_xyz(name):
    return FUNTYPE(getattr(lib, name + '_xyz'))

class Fun:
    def __init__(self, f):
        self.f = f

    def __call__(self, x):
        return self.f(x, 0.0)

    def __add__(self, other):
        return Fun(
