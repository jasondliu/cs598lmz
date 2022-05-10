from _struct import Struct
s = Struct.__new__(Struct)
s.size = 8
print(s.size)
print(s)

# 不能直接继承，可以直接实例化
from _struct import Struct
s = Struct('i?f')
print(s.size)
print(s)

from _struct import Struct
s = Struct('i?f')
print(s.pack(1, True, 2.0))
print(s.unpack(b'\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00@'))

from _struct import Struct
s = Struct('i?f')
print(s.pack(1, True, 2.0))
print(s.unpack(b'\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00@'))

from _struct import Struct
s = Struct('i?f')
print(s
