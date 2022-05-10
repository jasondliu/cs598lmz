import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def myfunc(x):
    return x+1

myfunc_c = FUNTYPE(myfunc)

print(myfunc_c(2))

#%%

import ctypes

class MyStruct(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

mystruct = MyStruct(1, 2)
print(mystruct.x)
print(mystruct.y)

#%%

import ctypes

class MyStruct(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

mystruct = MyStruct(1, 2)
print(mystruct.x)
print(mystruct.y)

mystruct.x = 3
print(mystruct.x)

#%%

import ctypes

class MyStruct(ctypes.Structure):
    _fields_ = [("x",
