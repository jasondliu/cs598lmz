import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

fun.__name__ = "fun"

def g():
    return fun

def h():
    def foo(fun=fun):
        return fun()
    return foo

class A(object):
    def __init__(self):
        self.fun = fun
    def f(self):
        return self.fun()

class B(object):
    def __init__(self):
        self.fun = fun
    def f(self):
        return self.fun()
    @classmethod
    def g(cls, fun=fun):
        return fun()

class C(object):
    def __init__(self):
        self.fun = fun
    def f(self):
        return self.fun()
    @staticmethod
    def g(fun=fun):
        return fun()

class D(object):
    def __init__(self):
        self.fun = fun
    def f(self):
        return self.fun()
    @property
    def g(self):
        return self.fun()


