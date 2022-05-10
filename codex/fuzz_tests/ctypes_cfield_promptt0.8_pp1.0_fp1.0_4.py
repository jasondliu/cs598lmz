import ctypes
# Test ctypes.CField
#
my_CField = ctypes.CField(ctypes.c_int, 0, "foo", False, False)
print my_CField
#
# Test ctypes.Structure
#
class MyStructure(ctypes.Structure):
    _fields_ = [my_CField]

print MyStructure
