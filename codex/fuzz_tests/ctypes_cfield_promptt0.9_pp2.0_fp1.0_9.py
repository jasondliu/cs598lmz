import ctypes
# Test ctypes.CField
class X(ctypes.Structure):
    _fields_ = [("_y", ctypes.CField)]
test_import("test_ctypes_CField", X, ['_y'])

# Test ctypes.Py_ssize_t
class SmallStructure(Structure):
    pass

# stores a Py_ssize_t as a c_int
SmallStructure._fields_ = [("size", Py_ssize_t)]
test_import("test_ctypes_Py_ssize_t_as_c_int", SmallStructure, ['size'])

# stores a Py_ssize_t as a c_long
SmallStructure._fields_ = [("size", Py_ssize_t)]
test_import("test_ctypes_Py_ssize_t_as_c_long", SmallStructure, ['size'])

SmallStructure._fields_ = [("size", Py_ssize_t), ("u", c_ulong)]
test_import("test_ctypes_Py_ssize_t_as_c_long_with
