import ctypes
# Test ctypes.CField
ctypes.CField(ctypes.c_int, "fieldName", "Doc")
ctypes.CField(ctypes.c_int, "fieldName")

# Test unions
class Letter(ctypes.Union):
    _fields_ = [
        ("upper", ctypes.c_char),
        ("lower", ctypes.c_char*2)
    ]

# Test ctypes.Structure
class Point(ctypes.Structure):
    _fields_ = [
        (Letter, "letters"),
        ("x", ctypes.c_int),
        ("y", ctypes.c_int),
    ]

# Test ctypes.PyCFuncPtr
ctypes.PyCFuncPtr(ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int), True)

# Test a number of ctypes.CData objects
ctypes.c_bool(True)
ctypes.c_byte(1)
ctypes.c_ubyte(1)
ctypes.c_short(1)
ctypes.c_
