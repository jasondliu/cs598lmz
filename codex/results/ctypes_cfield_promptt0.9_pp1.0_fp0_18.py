import ctypes
# Test ctypes.CField
c_bit_field = ctypes.CField(0, 3)
# Check if field is packed and alignment correct
class POINT(ctypes.Structure):
    _fields_ = [("x", c_bit_field),
                ("y", c_bit_field)]
assert_equal(ctypes.align(POINT), 1)
assert_equal(ctypes.sizeof(POINT), 1)
# Test ctypes.CStruct
c_struct = ctypes.CStruct(("x", c_bit_field),
                          ("y", c_bit_field))
# Check if struct is packed and alignment correct
class POINT(ctypes.Structure):
    _fields_ = [("point", c_struct)]
assert_equal(ctypes.align(POINT), 1)
assert_equal(ctypes.sizeof(POINT), 1)
