import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print('hello world')
    return 0

a = fun()
print(a)

c = fun()
print(c)
