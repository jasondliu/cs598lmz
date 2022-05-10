from _struct import Struct
s = Struct.__new__(Struct)
s.__init__(">I")
s.pack(12345)

with open("myfile.zip", "rb") as f:
    data = f.read()

start = 0
for i in range(3):
    start += 14
    fields = Struct("<IIIHH").unpack_from(data, start)

# struct.iter_unpack()
import struct
with open("myfile.zip", "rb") as f:
    for chunk in iter(lambda: f.read(24), b""):
        data = struct.unpack("<IIIHH", chunk)

# struct.pack_into()
import struct
s = struct.Struct("<I")
values = (1, 2, 3)
pack_into("<I", buf, 0, values[0])
pack_into("<I", buf, 4, values[1])
pack_into("<I", buf, 8, values[2])

# struct.pack_into()
import struct
buf = bytearray(18)
