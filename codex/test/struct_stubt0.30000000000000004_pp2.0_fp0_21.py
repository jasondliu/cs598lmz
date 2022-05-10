from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'I 2s f'
s.size = s.calcsize()
print(s.size)

import struct
print(struct.calcsize('I 2s f'))

# 可以用struct模块的pack函数来打包数据
print(struct.pack('>I', 10240099))

# 解压数据
print(struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80'))

# 内存中的字节流
# 在Python中，我们可以使用标准的struct模块来解决bytes和其他二进制数据类型的转换。
# 但是，在更高级的
