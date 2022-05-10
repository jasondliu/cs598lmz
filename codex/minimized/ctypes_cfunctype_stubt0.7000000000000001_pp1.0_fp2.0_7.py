def fun():
    print("hello")
from ctypes import CFUNCTYPE, cast, c_int
F = CFUNCTYPE(c_int, c_int, c_int)
def callit(fun, n, m):
    fun = cast(fun, F)
    print(fun(n, m))
callit(id(fun), 1, 2)
