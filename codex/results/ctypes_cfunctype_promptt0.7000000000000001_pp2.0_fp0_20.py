import ctypes
# Test ctypes.CFUNCTYPE
def func(a, b):
    return a+b

callback = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(func)
callback(1, 2)

# Test ctypes.Structure and ctypes.Union
class my_point(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_double),
        ('y', ctypes.c_double),
    ]

p = my_point(1, 2)
p.x
p.y

class my_color(ctypes.Union):
    _fields_ = [
        ('red', ctypes.c_ubyte),
        ('blue', ctypes.c_ubyte),
        ('green', ctypes.c_ubyte),
        ('all', ctypes.c_int32),
    ]

# Test ctypes.Array
class my_row(ctypes.Structure):
    _fields_ = [
        ('color', my_color * 5),
    ]
