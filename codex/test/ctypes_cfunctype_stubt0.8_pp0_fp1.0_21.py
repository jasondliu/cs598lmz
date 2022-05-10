import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 'OK'

result = fun()
print(result)

# 
import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
def fun(a):
    return a

f = FUNTYPE(fun)
result = f(3)
print(result)

# 
import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object)
def fun(a):
    return a
f = FUNTYPE(fun)
result = f(3)
print(result)

# 
import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object, ctypes.py_object)
def fun(a, b):
    return a, b

f = FUNTYPE(fun)
result = f(1, 2)
print(result)

# 
import ctypes
