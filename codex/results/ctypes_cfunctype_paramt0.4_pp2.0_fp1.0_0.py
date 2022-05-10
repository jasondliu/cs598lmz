import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def make_func(f):
    def g(x):
        return f(x)
    return FUNTYPE(g)

def make_func2(f):
    def g(x):
        return f(x)
    return FUNTYPE(g)

def make_func3(f):
    return FUNTYPE(f)

def make_func4(f):
    return FUNTYPE(lambda x: f(x))

def make_func5(f):
    return FUNTYPE(lambda x: f(x))

def make_func6(f):
    return FUNTYPE(lambda x: f(x))

def make_func7(f):
    return FUNTYPE(lambda x: f(x))

def make_func8(f):
    return FUNTYPE(lambda x: f(x))

def make_func9(f):
    return FUNTYPE(lambda x: f(x))

def make_func10(f):
    return FUNTYPE(lambda x: f(x
