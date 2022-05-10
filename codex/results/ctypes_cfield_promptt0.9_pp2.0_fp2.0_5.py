import ctypes
# Test ctypes.CField cast
struct = ctypes.Structure([('a', ctypes.c_short), ('b', ctypes.c_ushort)])
field = struct._fields[0][0]
assert ctypes.CField(field)._type_ is ctypes.c_short
try:
    field = object()
    ctypes.CField(field)
    raise AssertionError("Not raise exception")
except TypeError:
    pass
