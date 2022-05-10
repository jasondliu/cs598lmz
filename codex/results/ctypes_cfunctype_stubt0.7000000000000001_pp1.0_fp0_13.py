import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 'hello world'
fun()

# 4.2.2
def callback(index, value):
    return index + value
ctypes.pythonapi.PyObject_GetIter.restype = ctypes.py_object
ctypes.pythonapi.PyObject_GetIter.argtypes = [ctypes.py_object]
iter = ctypes.pythonapi.PyObject_GetIter(fun())
ctypes.pythonapi.PyIter_Next.restype = ctypes.py_object
ctypes.pythonapi.PyIter_Next.argtypes = [ctypes.py_object]
ctypes.pythonapi.PyNumber_Add.restype = ctypes.py_object
ctypes.pythonapi.PyNumber_Add.argtypes = [ctypes.py_object,ctypes.py_object]
for i in range(5):
    value = ctypes.pythonapi.PyIter_Next(iter)
    print(ctypes.pythonapi.PyNumber_Add(i, value))

# 4.2.3
import os
import sys
#print(dir(os))
