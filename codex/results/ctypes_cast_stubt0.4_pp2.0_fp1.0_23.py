import ctypes
ctypes.cast(ctypes.pointer(a), ctypes.POINTER(ctypes.c_int))
# <ctypes.LP_c_int object at 0x7f8d9c3d7b90>

# ctypes.POINTER() is a factory function that returns a new type object.
# The new type is a subclass of the first argument, and instances of the
# new type are pointers to the second argument.

# ctypes.pointer() is a function that creates a new pointer instance from
# a ctypes instance.

# ctypes.cast() is a function that creates a new ctypes instance from
# a pointer instance.

# Here's a simple example showing the difference between the two:

import ctypes

class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

point = POINT(10, 20)
point_ptr = ctypes.pointer(point)

print(point_ptr.contents)
# <__main__.POINT object at 0x7f
