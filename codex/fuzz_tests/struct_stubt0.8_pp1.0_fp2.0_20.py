from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i?f')
s.size

s = Struct('i?f')
s.size

data = s.pack(1, False, 2.3)
data

s.unpack(data)

data = bytes(range(12))
data

list(data)

list(range(1000))

list(range(5, 10))

list(range(5, 10, 2))

list(range(10, 1, -1))

list(range(10, 1, -2))

list(range(0, -10, -1))

list(range(0, -10, -2))

format = '5s 3x 8s f'

with open('packb.bin', 'wb') as f:
    f.write(Struct(format).pack(b'spam', b'eggs', 3.0))

data = open('packb.bin', 'rb').read()
data

list(data)

data[:5]

data[8:11]

data
