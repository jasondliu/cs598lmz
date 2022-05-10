from _struct import Struct
s = Struct.__new__(Struct)
data = s.pack(1, 2, 3)
n1, n2, n3 = s.unpack(data)
n1, n2, n3

data

from sys import intern
s1 = 'hello world'
s2 = 'hello world'
s1 is s2

s1 = intern('hello world')
s2 = intern('hello world')
s1 is s2


n1 = 257
s = Struct('i')
s.pack(n1)

s.pack(n1).decode('latin-1')

n2 = s.unpack(_[0])[0]
n2

n1 == n2

import struct
struct.pack('>I', 10240099)

struct.unpack('>IH', s)

for code in [b'BBBB', b'>BBBB', b'<BBBB', b'hhhh']:
    print(code, struct.pack('=4B', 1, 2, 3, 4))

for code in [b'BBBB', b'>BBBB', b'
