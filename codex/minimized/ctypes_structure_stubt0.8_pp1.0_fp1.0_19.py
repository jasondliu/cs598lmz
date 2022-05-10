import ctypes
class S(ctypes.Structure):
    x = ctypes.c_int
c = ctypes.c_int.from_address(id(S))
s = ctypes.py_object.from_address(ctypes.addressof(c))
print(s)
