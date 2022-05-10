import ctypes
# Test ctypes.CField.__str__()
print(str(ctypes.c_int.__dict__['value']))
print(str(ctypes.c_int.__dict__['_length_']))
print(str(ctypes.c_int.__dict__['_type_']))
# Test ctypes.CField.__repr__()
print(repr(ctypes.c_int.__dict__['value']))
print(repr(ctypes.c_int.__dict__['_length_']))
print(repr(ctypes.c_int.__dict__['_type_']))
