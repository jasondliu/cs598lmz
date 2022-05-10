from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.pack(1, 'ab'.encode('utf-8'), 2.7)

# _struct.Struct.pack_into(format, buffer, offset, v1, v2, ...)
# 向buffer中存放struct，从offset位置开始存放
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
buffer = bytearray(s.size)
s.pack_into(buffer, 0, 1, 'ab'.encode('utf-8'), 2.7)

# _struct.Struct.unpack(buffer)
# 从buffer中读取struct
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
buffer = bytearray(s.size)
s.pack_into(buffer, 0, 1, 'ab'.encode('utf-8'), 2.7)
s
