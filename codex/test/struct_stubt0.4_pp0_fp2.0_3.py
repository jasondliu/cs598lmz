from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.unpack(b'\x01\x00\x00\x00')

# 使用内建的struct模块
from struct import Struct
s = Struct('i')
s.unpack(b'\x01\x00\x00\x00')

# 如果你想在一个字节字符串上面执行大量的数据解析，你应该考虑为这些格式定义一个解析器类
from collections import namedtuple

# 定义解析器
Record = namedtuple('Record', ['kind', 'x', 'y'])

def parse_records(format, data):
    record_struct = Struct(format)
