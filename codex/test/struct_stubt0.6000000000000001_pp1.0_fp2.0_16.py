from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'I 8s f'
s.size = s.calcsize(s.format)

f = open('data.bin', 'w+')
packed_data = s.pack(1, 'test', 3.14)
print(repr(packed_data))
f.write(packed_data)
f.seek(0)
data = f.read()

print(data)
print(s.unpack(data))

