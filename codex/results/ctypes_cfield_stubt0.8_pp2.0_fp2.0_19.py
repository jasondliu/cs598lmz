import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
# Test with a NULL pointer
try:
    print(ctypes.c_int.from_address(0))
    raise Exception()
except ValueError:
    pass

s = S.from_address(0)
print(s.x)
print(s.x.value)
# Build a PyCField object, and test its flags
c = ctypes.c_int
print(c._type_)
print(c._name)
print(c._flags_)
# Test with a non-NULL pointer
s = S()
print(ctypes.c_int.from_address(s))
print(ctypes.c_int.from_address(s).value)
# Test with a non-NULL pointer
s.x = 123
print(ctypes.c_int.from_address(s))
print(ctypes.c_int.from_address(s).value)
# Create a new attribute on the structure, accessing it via a
# PyCField
c = ctypes.c_int.from_address(s)
setattr(s, 'x2',
