from _struct import Struct
s = Struct.__new__(Struct)
s.__dict__.update(Struct.__dict__)
s.format = '8s'
s.unpack(b'\x01\x02\x03\x04')
# (b'\x01\x02\x03\x04',)

import struct
struct.Struct(b'8s').unpack(b'\x01\x02\x03\x04')
# (b'\x01\x02\x03\x04',)


from _struct import Struct
print(Struct.__doc__)

Struct('x')

# 形状和大小必须与Python类型的顺序和字节数匹配
from _struct import Struct
_make_char = Struct('x')
_make_char.unpack(_make_char.pack('A'))
# ('A',)

# _make_int 是构建整数的重要函
