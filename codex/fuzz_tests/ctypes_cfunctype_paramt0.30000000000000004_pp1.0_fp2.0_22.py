import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_callback(a, b):
    print(a, b)
    return a + b

my_callback_c = FUNTYPE(my_callback)

#
# Callback with a structure
#

class MyStruct(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_int),
        ('y', ctypes.c_int),
        ('z', ctypes.c_int),
    ]

def my_callback_struct(a, b):
    print(a.x, b.x)
    return a.x + b.x

my_callback_struct_c = FUNTYPE(my_callback_struct)

#
# Callback with a structure pointer
#

class MyStructPtr(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_int),
        ('y', ctypes.c_int),
        ('z', ctypes.c_int),

