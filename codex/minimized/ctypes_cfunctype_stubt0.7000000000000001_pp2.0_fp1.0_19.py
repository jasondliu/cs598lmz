import ctypes
def fun():
    return 1
def fun_py(x):
    return x + 1
fun_py_addr = id(fun_py)
fun = ctypes.pythonapi.PyCFunction_NewEx(fun_py_addr, None, None)
