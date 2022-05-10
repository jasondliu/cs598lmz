import ctypes
ctypes.cast(1, ctypes.py_object)

# Src: https://docs.python.org/3/library/ctypes.html#ctypes.cast

# ctypes.cast(obj, typ)
# Cast an object to a type. The obj argument must be an object that can be interpreted as a pointer,
# and typ must be a ctypes type. The result is a new instance of typ pointing to the same memory block.

# The following example illustrates the difference between ctypes.cast() and ctypes.pointer():

# >>> from ctypes import *
# >>> i = c_int(42)
# >>> f = cast(pointer(i), POINTER(c_float))
# >>> f.contents.value
# 42.0
# >>> p = pointer(i)
# >>> p.contents.value
# 42
# >>> p.contents is i
# True
# >>> f.contents is i
# False
# >>> f.contents.value = 3.14
# >>> i.value
# 3
# >>> p.contents.value
# 3
# >>> f.
