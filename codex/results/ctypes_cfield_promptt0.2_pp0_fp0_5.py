import ctypes
# Test ctypes.CField
class CTest(ctypes.Structure):
    _fields_ = [
        ("a", ctypes.c_int),
        ("b", ctypes.c_int),
        ("c", ctypes.c_int),
    ]

ctypes.CField("a", ctypes.c_int, 0)
ctypes.CField("b", ctypes.c_int, 4)
ctypes.CField("c", ctypes.c_int, 8)

# Test ctypes.CField.from_address
ctypes.CField.from_address(ctypes.addressof(CTest()), "a", ctypes.c_int, 0)
ctypes.CField.from_address(ctypes.addressof(CTest()), "b", ctypes.c_int, 4)
ctypes.CField.from_address(ctypes.addressof(CTest()), "c", ctypes.c_int, 8)

# Test ctypes.CField.from_param
ctypes.CField.from_param(CTest(), "a
