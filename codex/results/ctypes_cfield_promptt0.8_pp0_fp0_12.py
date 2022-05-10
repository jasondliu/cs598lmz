import ctypes
# Test ctypes.CField
# Number of fields in a structure
assert isinstance(ctypes.CField.from_address(ctypes.Structure, 0).offset, int)
assert isinstance(ctypes.CField.from_address(ctypes.Structure, 1).offset, int)
assert isinstance(ctypes.CField.from_a
