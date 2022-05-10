import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# TODO: better way to expose this?
FUNCTIONS = {
    "f1": (FUNTYPE(1), [ctypes.c_int, ctypes.c_int]),
    "f2": (FUNTYPE(1), [ctypes.c_int, ctypes.c_int]),
    "f3": (FUNTYPE(1), [ctypes.c_int, ctypes.c_int]),
    "f4": (FUNTYPE(1), [ctypes.c_int, ctypes.c_int]),
    "f5": (FUNTYPE(1), [ctypes.c_int, ctypes.c_int]),
}


def f1(a, b):
    return a + b


def f2(a, b):
    return a * 2 + b * 2


def f3(a, b):
    return a * 1 + b * 2


def f4(a, b):
    return a * 2 + b * 1


def
