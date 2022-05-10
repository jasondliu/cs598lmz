from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('HHI')
s.size

s.pack(1, 2, 3)

f = open('data.bin', 'wb')
f.write(s.pack(1, 2, 3))
f.close()

f = open('data.bin', 'rb')
data = f.read()
f.close()

s.unpack(data)

f = open('data.bin', 'rb')
s.unpack_from(f.read())
f.close()

f = open('data.bin', 'rb')
for rec in iter(lambda: f.read(s.size), b''):
    print(s.unpack(rec))
f.close()
