import ctypes
ctypes.cast(0, ctypes.py_object)

#%%

from ctypes import *

class Test1(Structure):
    _fields_ = [("a", c_int),
                ("b", c_int)]
    
class Test2(Structure):
    _fields_ = [("a", c_int),
                ("b", c_int),
                ("c", c_int)]
    
#%%
p = pointer(Test1(1, 2))
q = cast(p, POINTER(Test2))
print(q.contents.a, q.contents.b, q.contents.c)

#%%

p = pointer(Test1(1, 2))
q = cast(p, POINTER(Test2))
print(q.contents.a, q.contents.b, q.contents.c)

#%%

p = pointer(Test1(1, 2))
q = cast(p, POINTER(Test2))
print(q.contents.a, q.contents.b, q.contents.c
