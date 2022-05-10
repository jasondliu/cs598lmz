from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('II')

def read_record(f):
    return s.unpack(f.read(s.size))

f = open('/tmp/mydata', 'rb')
import pprint
pprint.pprint(read_record(f))
pprint.pprint(read_record(f))
# (1, 123456789)
# (2, 987654321)

# 使用内置的struct模块实现
from struct import Struct
record_struct = Struct('<II')
record_struct.size
# 8
record_struct.unpack(b'\x01\x00\x00\x00\x07\x5b\xcd\x15')
# (1, 123456789)
# 编码读取的数据
record_struct.pack(1, 123456789)
# b'\x01\x00\x00\x00\x07\x5b\xcd\x
