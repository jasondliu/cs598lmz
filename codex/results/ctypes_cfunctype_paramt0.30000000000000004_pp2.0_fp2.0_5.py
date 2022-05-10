import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

class MyFunc(object):
    def __init__(self, func):
        self.func = func
        self.cfunc = FUNTYPE(func)
        self.cfunc.__name__ = func.__name__
        self.cfunc.__doc__ = func.__doc__

    def __call__(self, x):
        return self.cfunc(x)

    def __get__(self, obj, objtype):
        return self.cfunc

def myfunc(func):
    return MyFunc(func)

@myfunc
def mysin(x):
    return math.sin(x)

@myfunc
def mycos(x):
    return math.cos(x)

@myfunc
def mytan(x):
    return math.tan(x)

@myfunc
def myexp(x):
    return math.exp(x)

@myfunc
def mylog(x):
    return math.log(x)

@myfunc

