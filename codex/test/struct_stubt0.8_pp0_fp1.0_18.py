from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.size

from zipfile import ZIP_STORED, ZIP_DEFLATED
s = Struct.__new__(Struct)
s.__init__('<H')
hex(s.unpack(b'\x10\x27')[0])
print(s.unpack(b'\x10\x27')[0])

from _struct import pack, unpack
print(pack('>I', 10240099))
print(unpack('>IH', b'\x00\x9c@c'))

# 使用struct模块来解析网络数据
