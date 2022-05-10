import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def ccall(func):
    def x(*args):
        func(*args)
    return x

def callback(func):
    def x(*args):
        return func(*args)
    return x

@callback
def callback_func(x):
    return x * 2


@ccall
def cfunc(x, y):
    pass

@ccall
def func(x, y, z):
    pass

@ccall
def func(x, y, z, z1):
    pass

@ccall
def func(x, y, z, z1, z2):
    pass

@ccall
def func(x, y, z, z1, z2, z3):
    pass

# For genwrapper.py
@ccall
def func(x, y, z, z1, z2, z3, z4):
    pass


@ccall
def func(x, y, z, z1, z2, z3, z4, z5
