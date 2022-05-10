import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

# Accessing a field of a custom subclass does not raise a Value Error
class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]


class T(S):
    _fields_ = [('y', ctypes.c_int)]

print(T.x)
print(type(T.x))
print(T.x.offset)
print(issubclass(type(T.x), ctypes.CField))
print(T._field_index)
