import ctypes
ctypes.cast(ctypes.pointer(c_int(0)), ctypes.POINTER(ctypes.c_int))

# Convert None to NULL pointer without error
for arg in [None, ctypes.c_int()]:
    print(arg)

# Keyword and positional arguments
ctypes.c_int(1)
ctypes.c_int(value=1)

# Create ctypes instance from pointer
class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_ulong), ("y", ctypes.c_ulong)]

point = POINT(10, 20)
ctypes.pointer(point)
p = ctypes.pointer(point)
p.contents

# create ctypes instance from integer address
ctypes.cast(id(point), ctypes.POINTER(POINT))

# Create ctypes array from Python list
array_type = ctypes.c_int * 3
array_type(*range(3))

# Create ctypes array from pointer and size
array_type = ctypes.c_double * 3
array
