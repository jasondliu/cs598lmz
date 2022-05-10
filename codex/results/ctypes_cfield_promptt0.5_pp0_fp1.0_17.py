import ctypes
# Test ctypes.CField
assert ctypes.CField(ctypes.c_int, "field")
# Test ctypes.CField.from_address
assert ctypes.CField.from_address(0, ctypes.c_int)
# Test ctypes.CField.from_buffer
assert ctypes.CField.from_buffer(ctypes.c_int(0), 0)
# Test ctypes.CField.from_param
assert ctypes.CField.from_param(ctypes.c_int(0))
# Test ctypes.CField.in_dll
assert ctypes.CField.in_dll(ctypes.CDLL(None), "foo")
# Test ctypes.CField.offset
assert ctypes.CField.offset
# Test ctypes.CField.value
assert ctypes.CField.value
# Test ctypes.CField.__get__
assert ctypes.CField.__get__(ctypes.c_int(0), None, None)
# Test ctypes.CField.__set__
ctypes.CField.__set__(ctypes.c
