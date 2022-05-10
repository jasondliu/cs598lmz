import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

    # This is optional
    _fields_ = [
        ('x', ctypes.c_int),
        ('y', ctypes.c_int),
    ]

class T(ctypes.Structure):
    _fields_ = [
        ('a', S * 2)
    ]

a = S(1, 2)
b = S(3, 4)
t = T((a, b))
print t.a[0].x
print t.a[0].y
print t.a[1].x
print t.a[1].y

# Now you can use t.a[0] and t.a[1] as regular C structures.
# You can also use ctypes.byref(t.a[0]) to pass the address of t.a[0] to a
# C function.
#
# Note that this has nothing to do with ctypes: it's just how C structures are
# laid out in memory.  The C compiler doesn't care what you use as the name of

