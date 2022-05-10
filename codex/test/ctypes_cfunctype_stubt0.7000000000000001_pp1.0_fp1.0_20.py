import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

assert fun() == 1

# test mangled name
def fun():
    pass

assert fun.__name__ == 'fun'

# test staticmethod
class A:
    @staticmethod
    def f():
        pass

assert A.f.__name__ == 'f'

# test classmethod
class A:
    @classmethod
    def f(cls):
        pass

assert A.f.__name__ == 'f'

# test __kwdefaults__
def f(x, y=0):
    pass

