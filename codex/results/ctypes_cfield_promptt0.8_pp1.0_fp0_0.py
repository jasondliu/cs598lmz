import ctypes
# Test ctypes.CField
type_ = ctypes.c_int64
field = ctypes.CField.from_address(type_, 0, type_)
# Check that there are no errors
value = type_(1)


# Check that there are no errors
ctypes.CField.from_address(type_, ctypes.sizeof(type_), type_)


class Test(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.c_int),
                ("d", ctypes.c_int),
                ("e", ctypes.c_int),
                ("f", ctypes.c_int),
                ("g", ctypes.c_int),
                ("h", ctypes.c_int),
                ("i", ctypes.c_int),
                ("j", ctypes.c_int),
                ("k", ctypes.c_int),
                ("l", ctypes.c_int),
                ("m", ctypes.c_int),
               
