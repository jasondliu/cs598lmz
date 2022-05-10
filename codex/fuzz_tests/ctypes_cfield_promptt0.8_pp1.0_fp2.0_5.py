import ctypes
# Test ctypes.CField

# Test fields with size, align and offset specified
class FIELD(ctypes.Structure):
    _fields_ = (
        ('test', ctypes.c_char * 7, 2, 4),
        ('test2', ctypes.c_char * 7, 3, 5),
    )

FIELD_ref = b"\x00\x01\x02\x03\x04\x05\x06" * 2
field = FIELD()
field.test = b"foo"
field.test2 = b"bar"
assert ctypes.string_at(ctypes.byref(field), ctypes.sizeof(field)) == FIELD_ref
