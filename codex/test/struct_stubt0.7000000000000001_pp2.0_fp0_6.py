from _struct import Struct
s = Struct.__new__(Struct)
s.size = 10
s.format = 'iif'
s.unpack('\x12\x34\x56\x78\x9a\xbc\xde\xf0\x00\x00')

# 实例化：
from struct import Struct
s = Struct('iif')
s.size
s.unpack('\x12\x34\x56\x78\x9a\xbc\xde\xf0\x00\x00')

s = Struct('>iif')
s.size
s.unpack('\x12\x34\x56\x78\x9a\xbc\xde\xf0\x00\x00')

# 封装：
from struct import Struct
def write_records(records, format, f):
    record_struct = Struct(format)
    for r in records:
        f.write(record_struct.pack(*r))
        
