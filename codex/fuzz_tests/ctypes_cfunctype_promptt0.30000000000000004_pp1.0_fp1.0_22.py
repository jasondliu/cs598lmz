import ctypes
# Test ctypes.CFUNCTYPE

def func(x):
    return x + 1

f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(func)

print f(1)
print f(2)
print f(3)

# Test ctypes.POINTER

class POINTER(ctypes.c_int):
    _type_ = "P"

class S(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

s = S(1, 2)
ps = POINTER(S)

print ctypes.cast(ps, ctypes.POINTER(ctypes.c_int)).contents
print ctypes.cast(ps, ctypes.POINTER(ctypes.c_int)).contents.value
print ctypes.cast(ps, ctypes.POINTER(ctypes.c_int)).contents.value == s
print ctypes.cast(ps, ctypes.POINTER(ctypes.c_int)).contents.value
