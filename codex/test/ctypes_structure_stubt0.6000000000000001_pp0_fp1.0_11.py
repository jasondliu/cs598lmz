import ctypes

class S(ctypes.Structure):
    x = ctypes.c_short
    y = ctypes.c_int
    z = ctypes.c_long
    t = ctypes.c_double

a = S()
a.x, a.y, a.z, a.t

# Convert the Python object to a ctypes object
b = ctypes.cast(id(a), ctypes.POINTER(S))

# Now we can access the fields of the ctypes object
b.contents.x, b.contents.y, b.contents.z, b.contents.t

b.contents.x = -1
b.contents.y = -2
b.contents.z = -3
b.contents.t = -4

# And the original Python object was modified!
a.x, a.y, a.z, a.t

# If we change the Python object, the ctypes object is also modified
a.x = 1
a.y = 2
a.z = 3
a.t = 4

