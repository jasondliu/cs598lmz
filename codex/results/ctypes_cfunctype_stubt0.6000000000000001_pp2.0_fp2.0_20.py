import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print("hello world")
    return 42

f = fun
print(f())
print(f.__name__)
