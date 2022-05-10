from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i', '<')
s.unpack(b'\x12\x34\x56\x78')

# 未知格式（不支持）
# print(s.unpack(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'))

# 打包数据
# 对于复杂的数据结构，需要先把复杂的数据结构拆分成简单的结构，再打包成字符串，再写入文件，再用struct解包
# 这里
