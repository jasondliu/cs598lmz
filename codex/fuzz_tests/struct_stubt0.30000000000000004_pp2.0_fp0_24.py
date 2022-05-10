from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i?f')
s.size

s = Struct('i?f')
s.size

import struct
struct.calcsize('i?f')

# 可以使用标准的格式说明符来指定结构的字节顺序
s = Struct('>i?f')
s.size

# 在一个结构中，每个字段都由一个元组来指定，元组的第一个元素是一个格式说明符，第二个元素是一个字段名
# 如果没有提供字段名，那么将使
