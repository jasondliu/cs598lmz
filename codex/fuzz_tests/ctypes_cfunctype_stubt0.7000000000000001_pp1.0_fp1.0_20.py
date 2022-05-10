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

assert f.__kwdefaults__ == {'y': 0}

# test __annotations__
def f(x: int):
    pass

assert f.__annotations__ == {'x': int}

# test __closure__ (empty)
def f():
    pass

assert f.__closure__ is None

# test __closure__ (non-empty)
a = b = 1
def fun():
    pass

assert fun.__closure__[0].cell_contents ==
