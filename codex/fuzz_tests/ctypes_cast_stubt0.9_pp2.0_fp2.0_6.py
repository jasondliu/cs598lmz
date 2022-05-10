import ctypes
ctypes.cast(DatePtr(ctypes.byref(d)), ctypes.POINTER(ctypes.c_int)).contents

# Floating-point values are easy.
f = ctypes.c_float(1.0)
f
ctypes.addressof(f)
f.value

f.value = 2.0
print(f.value)
f.value = 2.345
print(f.value)

# to get properties of complex C structures, use containers as struct and union
# this is a struct
class Point(ctypes.Structure):
  _fields_ = [("x", ctypes.c_float),
              ("y", ctypes.c_float)]

# this is a union
class Point2(ctypes.Union):
  _fields_ = [("x", ctypes.c_float),
              ("y", ctypes.c_float)]

p = Point(1.0, 2.0)
print(p.x)
print(p.y)

p2 = Point2(1.0)
print(p2.x) # prints
