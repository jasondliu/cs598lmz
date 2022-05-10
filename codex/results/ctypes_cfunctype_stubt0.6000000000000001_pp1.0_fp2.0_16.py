import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 'hello world'

print fun()

# 如果想要让这个函数能够在没有 GIL 的情况下运行，可以使用@nogil 装饰器
from numba import njit
@njit(nogil=True)
def f(x):
    return x * x

print f(5)
# 这个函数可以在多线程中运行，而不会产生不可预料的结果。
# 此外，你可以用这个装饰器去装饰你的类，这样所有的方法都会被装饰。

# 你还
