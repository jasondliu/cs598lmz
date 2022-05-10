from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.unpack(b'\x01\x00\x00\x00')

# struct.Struct.unpack_from(buffer, offset=0)
# 从buffer中按照格式解析出数据，offset是偏移量
# 返回解析出的数据元组
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.unpack_from(b'\x01\x00\x00\x00\x02\x00\x00\x00', 4)

# struct.Struct.iter_unpack(buffer)
# 从buffer中按照格式解析出数据，返回解析出的数据迭代器
