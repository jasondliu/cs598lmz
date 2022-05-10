from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.size

s.pack(1, b'ab', 2.7)

s.unpack(_)

s.unpack_from(b'\x00\x00\x00\x01ab\x00\x00\x9a\x99\x99\x99\x99\x9a', 0)

s.unpack_from(b'\x00\x00\x00\x01ab\x00\x00\x9a\x99\x99\x99\x99\x9a', 4)

s.iter_unpack(b'\x00\x00\x00\x01ab\x00\x00\x9a\x99\x99\x99\x99\x9a')

for item in _:
    print(item)

# %load code/struct_iter_unpack.py
import struct

def iter_unpack(fmt, buf):
    s = struct.Struct(fmt)
    return
