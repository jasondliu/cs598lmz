import ctypes
# Test ctypes.CField
#
# ctypes.CField represents a structure field in a ctypes Structure.
#
# ctypes.CField instances have the following attributes:
#   - name: the field name
#   - type: the field type
#   - offset: the field offset in bytes
#
# ctypes.CField instances are returned by
# Structure.get_fields() and Union.get_fields()
#
# ctypes.CField instances can be used for creating a
# structure with the same layout by calling
# Structure.from_fields() or Union.from_fields()
#

class S(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int)]

s = S()

assert [f.name for f in s.get_fields()] == ["x", "y"]
assert [f.type for f in s.get_fields()] == [ctypes.c_int, ctypes.c_int]
assert [f.offset for f in s.get_fields()] == [0, ctypes.
