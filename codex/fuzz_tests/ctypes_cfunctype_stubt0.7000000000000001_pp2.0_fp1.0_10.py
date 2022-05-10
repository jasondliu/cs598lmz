import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print('fun')
    return '123'

fun()

print(fun())

@FUNTYPE
def fun2(a, b):
    print(a, b)
    return a * b

fun2(3, 5)
print(fun2(3, 5))
