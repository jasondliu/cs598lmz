import ctypes
# Test ctypes.CFUNCTYPE works as intended
def make_c_callable(func, restype, argtypes):
    return ctypes.CFUNCTYPE(restype, *argtypes)(func)

@make_c_callable(None, ctypes.c_int, [ctypes.c_int, ctypes.c_double])
def f(a: int, b: float):
    print(a, b)

f(1, 1)
f(a=1, b=1)
f(b=1, a=1)
f(a=1, 1)
f(1, b=1)
f(b=1, 1)
# Test ctypes.CFUNCTYPE with a classmethod
class C:
    @classmethod
    @make_c_callable(None, ctypes.c_int, [ctypes.c_int, ctypes.c_double])
    def f(cls, a: int, b: float):
        print(cls, a, b)

C.f(1, 1)
C.f(a=1
