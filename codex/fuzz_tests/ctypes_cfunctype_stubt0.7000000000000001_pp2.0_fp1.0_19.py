import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

v = fun()

def fun_py(x):
    return x + 1

fun_py(1)

fun_py_addr = id(fun_py)

print(fun_py_addr)
print(id(fun_py))

def fun_py(x):
    return x + 2

print(id(fun_py))

ctypes.pythonapi.PyCFunction_NewEx.argtypes = (ctypes.py_object, ctypes.py_object, ctypes.py_object)
ctypes.pythonapi.PyCFunction_NewEx.restype = ctypes.py_object

fun = ctypes.pythonapi.PyCFunction_NewEx(fun_py_addr, None, None)

v = fun(1)

print(v)

print(id(fun))
