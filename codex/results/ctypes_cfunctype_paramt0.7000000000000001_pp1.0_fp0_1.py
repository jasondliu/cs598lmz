import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int,ctypes.c_double,ctypes.c_double,ctypes.c_double,ctypes.c_double,ctypes.c_double)

class myFunctor(object):
    def __init__(self, funtype, func):
        self.funtype = funtype
        self.func = func
    def __call__(self, *args):
        return self.funtype(self.func)(*args)


def fun_c(a,b,c,d,e):
    return c*d
fun = myFunctor(FUNTYPE,fun_c)

class myFunctor2(object):
    def __init__(self, funtype, func):
        self.funtype = funtype
        self.func = func
    def __call__(self, *args):
        return self.funtype(self.func)(*args)


def fun_c2(a,b,c,d,e):
    return e*d
fun2 = myFunctor(FUNTYPE,fun_c2)
</code
