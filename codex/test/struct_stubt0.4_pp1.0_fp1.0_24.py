from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.size

s.pack(1, 'ab', 2.7)

s.unpack(_)

s.unpack_from(bytes(range(12)), 4)

# 如果不想使用标准的字节序、字符大小和对齐方式，可以使用
# 关键字参数来更改它们，比如
s = Struct('>I 2s f')
s.pack(1, 'ab'.encode('utf-8'), 2.7)

# 对于简单的结构体，可以使用字节对象的
# 方法来代替，比如
import struct

