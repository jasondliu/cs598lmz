from _struct import Struct
s = Struct.__new__(Struct)
s.format = '<dd'
s.size = calcsize(s.format)

with open('data.bin', 'rb') as f:
    for x, y in iter(lambda: f.read(s.size), ''):
        x, y = s.unpack(x)
        print x, y
