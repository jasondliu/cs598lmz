import ctypes
# Test ctypes.CField and ctypes.Field
class POINT(ctypes.Structure):
    _pack_ = 4
    _fields_ = [("x", ctypes.c_uint16, 11),
                ("y", ctypes.c_uint16, 11)]

class POINT_UNION(ctypes.Union):
    _pack_ = 4
    _fields_ = [("pt", POINT, 16),
                ("point", ctypes.c_uint32)]

buf = ctypes.create_string_buffer(ctypes.sizeof(POINT_UNION))
p = POINT_UNION()
p.pt.x = 0x7FF
p.pt.y = 0x7FF
ctypes.memmove(ctypes.addressof(buf), ctypes.addressof(p), ctypes.sizeof(POINT_UNION))
assert buf.raw == b'\x00\x7f\xff\xff\xff\xff'

p = POINT_UNION()
p.point = 0xFFFFFFFF
ctypes.memmove(ctypes.addressof
