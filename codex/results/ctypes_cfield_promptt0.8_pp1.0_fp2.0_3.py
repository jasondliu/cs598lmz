import ctypes
# Test ctypes.CField
class X(ctypes.Structure):
    _fields_ = [("one", ctypes.c_double),
                ("two", ctypes.c_int),
                ("three", ctypes.c_int),
                ("four", ctypes.c_uint),
                ("five", ctypes.c_longlong),
                ("six", ctypes.c_float),
                ("seven", ctypes.c_double),
                ("eight", ctypes.c_ulonglong)]

test = X()
print("X:", repr(test))
print("ctypes.CField:", repr(test.six))
print("ctypes.CField:", repr(test.four))
print("ctypes.CField:", repr(test.eight))

# Test ctypes.CArray
A = ctypes.c_int * 16
test = A()
print("A:", repr(test))
print("A:", repr(test[::2]))
print("A:", repr(test[9:12]))

# Test ctypes.CData
print("ctypes
