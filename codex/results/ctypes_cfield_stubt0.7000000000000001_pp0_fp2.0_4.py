import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

# descriptor for the 'x' field
fd = S.x
fd.__objclass__ = S

# bf_get read-only attribute
bf_get = ctypes.CField.__get__

print(bf_get(fd, None, S))
print(bf_get(fd, None, S) is S._fields_[0][1])
try:
    bf_get(fd, None, 42)
except TypeError:
    print("TypeError")
