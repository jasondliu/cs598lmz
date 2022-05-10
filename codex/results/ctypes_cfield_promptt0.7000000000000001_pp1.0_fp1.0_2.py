import ctypes
# Test ctypes.CFields
import ctypes.wintypes

# ctypes.CFields.from_address()
class C(ctypes.Structure):
    _fields_ = [
        ("a", ctypes.c_int),
        ("b", ctypes.c_char),
    ]

buf = ctypes.create_string_buffer(4)
buf[0] = b"\x01"
buf[1] = b"\x02"
buf[2] = b"\x03"
buf[3] = b"\x04"

c = C.from_buffer(buf)
# CFields.from_buffer()
c = C.from_buffer(buf, 1)

# CFields.from_buffer_copy()
c = C.from_buffer_copy(buf)

# CFields.from_address()
c = C.from_address(ctypes.addressof(buf))

# CFields.in_dll()
c = C.in_dll(ctypes.CDLL(None), "c")

# Test c
