import ctypes
ctypes.cast(id(x), ctypes.py_object).value

#%%
x = "Hello"
ctypes.cast(id(x), ctypes.py_object).value

#%%
import sys

sys.getrefcount(x)

#%%
class A:
    def __init__(self):
        pass

a = A()

#%%
type(a)

#%%
a.__class__

#%%
type(a) == a.__class__

#%%
type(A)

#%%
type(type)

#%%
type(type(a))

#%%
type(type(type(a)))

#%%
type(type(type(type(a))))

#%%
type(type(type(type(type(a)))))

#%%
type(type(type(type(type(type(a))))))

#%%
class B:
    def __init__(self):
        pass

class C(B):
    def __init__(self):
        super().__init__
