import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def func(a, b):
    return a + b

cfunc = FUNTYPE(func)
print(cfunc(1, 2))

# 将C函数转换为Python函数
# 将C函数转换为Python函数，可以使用ctypes.pythonapi模块。
# ctypes.pythonapi.PyCFunction_NewEx.argtypes = (ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object, ctypes.py_object, ctypes.py_object), ctypes.py_object, ctypes.py_object, ctypes.py_object)
# ctypes.pythonapi.PyCFunction_NewEx.restype = ctypes.py_object
#
# def func(a, b):
#     return a + b
#
# cfunc = ctypes.python
