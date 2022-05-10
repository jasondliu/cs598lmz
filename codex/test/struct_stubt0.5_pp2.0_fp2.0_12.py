from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('!I')
print(s.size)
print(s.pack(10))
print(s.unpack(b'\x0a\x00\x00\x00'))

from collections import namedtuple
Point = namedtuple('Point', 'x,y')
p = Point(11, y=22)
print(p[0] + p[1])
print(p.x + p.y)
print(p)

print(isinstance(p, tuple))

from array import array
a = array('I', range(3))
print(a)

from base64 import b64encode
from base64 import b64decode

s = b64encode(b'binary\x00string')
print(s)
print(b64decode(s))

from collections import deque
d = deque(range(10), maxlen=10)
print(d)
d.rotate(3)
print(d)
d.rotate(-4)
print(d)
