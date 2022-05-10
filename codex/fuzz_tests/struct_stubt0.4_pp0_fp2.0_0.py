from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'I 2s f'
s.size = s.calcsize(s.format)
print(s.size)

with open('data.bin', 'rb') as f:
    data = f.read()

print(len(data))

unpacker = Struct('I 2s f')
for offset in range(0, len(data), unpacker.size):
    print(unpacker.unpack_from(data, offset))
