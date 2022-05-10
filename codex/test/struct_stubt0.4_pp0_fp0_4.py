from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>H')
s.size

# 使用标准库中的struct模块
from struct import Struct
s = Struct('>H')
s.size

# 内置函数bytes
b = bytes((0, 1, 2, 3))
b

# 创建空的bytes
b = bytes(4)
b

# 内置函数bytearray
ba = bytearray((0, 1, 2, 3))
ba

# 创建空的bytearray
ba = bytearray(4)
ba

# 内置函数memoryview
mv = memoryview(b'abcefg')
mv

# 创建空的memoryview
mv = memoryview(bytearray(4))
mv

# 使用memoryview查看字节
