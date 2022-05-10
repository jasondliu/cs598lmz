from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('4s')

f = open('binary-data.bin', 'rb')
data = f.read()
f.close()

offset = 0
while len(data) >= offset + 4:
    header = s.unpack_from(data, offset)
    print(header)
    offset += 4

# (b'1234',)
# (b'data',)
# (b'=\x00\x00',)
