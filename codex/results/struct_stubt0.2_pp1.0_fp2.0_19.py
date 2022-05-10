from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.size

# 使用struct模块来解决字节序问题
import struct
orig_data = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
print(struct.unpack('<ccIIIIIIHH', orig_data))

# 使用struct模块来解决字节序问题
import struct
s = struct.Struct('>I')
s.pack(10240099)

# 使用struct模块来解决字节序问
