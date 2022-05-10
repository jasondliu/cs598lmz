import ctypes
ctypes.cast(3, ctypes.py_object)
# ctypes.cast(3, ctypes.c_int)
# ctypes.cast(3, ctypes.py_object)
# ctypes.cast(3, ctypes.py_object) + ctypes.cast(3, ctypes.py_object)
a = ctypes.cast(3, ctypes.py_object)
type(a)
a()
type(1)
type(type(1))
b = __builtins__.abs
type(b)
type(b(1))
a = __builtins__.abs
type(a)
a(1)
type(a)
type(a(1))
a(1) + 1
a(1) + a(1)
type(a(1))
f = __new__(type, 3)
dir(f)
getattr(f, 'func_closure')
def g(x):
    return x
g.__code__.co_consts
g.__code__.co_varnames
g.func_closure[0]

