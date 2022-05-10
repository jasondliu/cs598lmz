import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p)


def print_function_type(func):
    print("%s : %s" % (func, type(func)))
    print("%s : %s" % (func.__name__, type(func.__name__)))
    print("%s : %s" % (func.__name__.encode('ascii'), type(func.__name__.encode('ascii'))))
    print("%s" % FUNTYPE.argtypes)
    print("%s" % FUNTYPE.argtypes[0])
    print("%s" % FUNTYPE.argtypes[1])
    print("%s" % FUNTYPE.argtypes)
    print("%s" % FUNTYPE.argtypes[0])
    print("%s" % FUNTYPE.argtypes[1])
    f = FUNTYPE(func)
    # print("%s" % f)
    # print("%s" % f())
    return f


def test_function_type():
    def f(
