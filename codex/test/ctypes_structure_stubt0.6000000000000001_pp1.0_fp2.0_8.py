import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

class R(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

a = (S * 2)()
b = (R * 2)()

a[0].x = 1
a[0].y = 2
a[1].x = 3
a[1].y = 4

b[0].x = 5
b[0].y = 6
b[0].z = 7
b[1].x = 8
b[1].y = 9
b[1].z = 10

a_buf = ctypes.string_at(a, ctypes.sizeof(a))
b_buf = ctypes.string_at(b, ctypes.sizeof(b))

x = S()
y = R()

ctypes.memmove(ctypes.byref(x), a_buf, ctypes.sizeof(x))
