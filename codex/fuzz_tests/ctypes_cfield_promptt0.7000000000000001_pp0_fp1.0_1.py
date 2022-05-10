import ctypes
# Test ctypes.CField
class CFoo(ctypes.LittleEndianStructure):
    _pack_ = 1
    _fields_ = [("bar", ctypes.c_uint16)]
# Test ctypes.Union
class UFoo(ctypes.LittleEndianUnion):
    _pack_ = 2
    _fields_ = [("bar", ctypes.c_uint16),
                ("baz", ctypes.c_uint32)]
# Test ctypes.Struct
