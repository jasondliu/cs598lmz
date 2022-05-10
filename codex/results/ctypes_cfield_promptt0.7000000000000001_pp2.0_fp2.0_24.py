import ctypes
# Test ctypes.CField
i = ctypes.c_int(42)
f = ctypes.c_float(3.14)
o = ctypes.c_void_p(id(i))

class Test(ctypes.Structure):
    _fields_ = [
        ('i', ctypes.c_int),
        ('f', ctypes.c_float),
        ('o', ctypes.c_void_p),
    ]

t = Test.from_buffer_copy(i)
print(t.i)
print(t.f)
print(t.o)
print(type(t.o))
print(type(ctypes.byref(t)))

class Test1(ctypes.Structure):
    _fields_ = [
        ('i', ctypes.c_int),
        ('f', ctypes.c_float),
        ('o', ctypes.c_void_p),
    ]

t1 = Test.from_buffer_copy(i)
print(t1.i)
print(t1.f)
print(t1.o
