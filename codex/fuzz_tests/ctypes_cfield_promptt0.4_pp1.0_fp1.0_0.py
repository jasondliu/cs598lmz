import ctypes
# Test ctypes.CField
assert ctypes.CField(ctypes.c_int, "foo") == ctypes.c_int.in_dll(ctypes.pythonapi, "foo")
# Test ctypes.CField.__get__
assert ctypes.CField(ctypes.c_int, "foo").__get__(None) == ctypes.c_int.in_dll(ctypes.pythonapi, "foo")
# Test ctypes.CField.__set__
ctypes.CField(ctypes.c_int, "foo").__set__(None, 42)
assert ctypes.c_int.in_dll(ctypes.pythonapi, "foo").value == 42
# Test ctypes.CField.__delete__
ctypes.CField(ctypes.c_int, "foo").__delete__(None)
assert ctypes.c_int.in_dll(ctypes.pythonapi, "foo").value == 0

# Test ctypes.CField.from_address
assert ctypes.CField(ctypes.c_int, "foo").from_address(id(ct
