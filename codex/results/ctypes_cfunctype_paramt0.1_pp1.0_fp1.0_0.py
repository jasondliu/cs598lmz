import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def my_callback(x):
    print("my_callback called with", x)
    return x + 1

my_callback_c = FUNTYPE(my_callback)

my_callback_c(1)

#%%
import ctypes

class MyClass(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

my_class = MyClass(1, 2)

print(my_class.x)
print(my_class.y)

#%%
import ctypes

class MyClass(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

my_class = MyClass(1, 2)

print(my_class.x)
print(my_class.y)

my_class.x = 3
my_class.y = 4

print(my_class.x)
