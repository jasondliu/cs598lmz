from _struct import Struct
s = Struct.__new__(Struct)
s.format = '0s10s'
s.size = s.calcsize(s.format)

def read_record(stream):
    return s.unpack(stream.read(s.size))

with open('test.bin', 'rb') as f:
    for n in range(3):
        print(read_record(f))

# (b'', b'\x00\x00\x00\x00\x00')
# (b'', b'\x00\x00\x00\x00\x00')
# (b'', b'\x00\x00\x00\x00\x00')
</code>

