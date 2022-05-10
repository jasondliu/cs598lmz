import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
def fun():
    print("hello world")
c_fun = FUNTYPE(fun)
py_fun = ctypes.pythonapi.PyCFunction_NewEx(c_fun, None, None)
