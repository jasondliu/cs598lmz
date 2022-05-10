from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>i')
s.unpack(b'\x00\x00\x00\x00')

# 使用struct模块来解析二进制文件
# 使用struct模块来解析二进制文件
# 在很多场合，你需要将一个二进制文件解析为一个结构化的格式。
# 例如，你可能想解析一个Windows的.bmp或者.jpg文件，或者一个Python的.pyc文件。
# 在这些情况下，你需要分析二进制数
