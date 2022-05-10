import ctypes
ctypes.cast(1, ctypes.c_void_p).value

import struct
def unpack_from(fmt, data, offset = 0):
    size = struct.calcsize(fmt)
    return struct.unpack(fmt, data[offset:offset+size])

# test
u = unpack_from('I', b'12345678', 0)
print(u)
u = unpack_from('I', b'12345678', 2)
print(u)
u = unpack_from('I', b'12345678', 6)
print(u)
