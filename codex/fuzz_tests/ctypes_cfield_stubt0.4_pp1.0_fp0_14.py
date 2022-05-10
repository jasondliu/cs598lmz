import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class X(ctypes.c_int):
    pass

print(type(ctypes.c_int))
print(type(ctypes.c_int(1)))
print(type(ctypes.c_int.in_dll(None, "foo")))
print(type(ctypes.c_int.from_address(0)))
print(type(ctypes.c_int.from_buffer(b"\x01\x00\x00\x00")))
print(type(ctypes.c_int.from_buffer_copy(b"\x01\x00\x00\x00")))
print(type(ctypes.c_int.from_param(1)))
print(type(ctypes.c_int.in_dll(None, "foo")))
print(type(ctypes.c_int.in_dll(None, "foo").value))
print(type(ctypes.c_int.in_dll(None, "foo")._objects))
print(type(ctypes.c_int.in_dll(None, "foo
