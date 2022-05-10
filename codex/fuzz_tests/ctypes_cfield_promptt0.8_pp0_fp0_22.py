import ctypes
# Test ctypes.CField.from_address

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.c_int)]

address = ctypes.addressof(X())
field = ctypes.CField.from_address(address)
assert field is X._fields_[0]
assert field.offset == 0

field = ctypes.CField.from_address(address + 4)
assert field is X._fields_[1]
assert field.offset == 4

field = ctypes.CField.from_address(address + 8)
assert field is X._fields_[2]
assert field.offset == 8

try:
    field = ctypes.CField.from_address(address + 12)
except ValueError:
    pass
else:
    raise Exception

try:
    field = ctypes.CField.from_address(address - 1)
except ValueError:
    pass
else:
    raise Exception
