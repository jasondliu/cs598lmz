import ctypes
# Test ctypes.CField
class c_fp(ctypes.Structure):
    _fields_ = [
        ("exponent", ctypes.c_int),
        ("mantissa", ctypes.c_int)
    ]

##ctypes.CField(c_fp, "exponent", 0, ctypes.sizeof(c_fp) * 8 - 1)
##ctypes.CField(c_fp, "mantissa", 1, ctypes.sizeof(c_fp) * 8 - 32)
# FIXME: The following test is commented out because it is broken.
##ctypes.CField(c_fp, "exponent", ctypes.sizeof(c_fp) * 8 - 1, 0)
##ctypes.CField(c_fp, "mantissa", ctypes.sizeof(c_fp) * 8 - 32, 1)

# Test ctypes.CField.__get__
class c_fp2(ctypes.Structure):
    _fields_ = [
            ("exponent", ctypes.c_uint, 15),
            ("mantissa", c
