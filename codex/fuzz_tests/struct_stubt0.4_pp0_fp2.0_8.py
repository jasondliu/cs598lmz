from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>H')
s.size

# 使用struct模块打包和解包二进制数据
import struct
data = struct.pack('>i4sh', 7, b'spam', 8)
data

struct.unpack('>i4sh', data)

# 二进制数据的拆分
data = b'Hello World'
data[0:5]

data[0:5] = b'Hallo'
data

# 使用memoryview处理二进制数据
import array
numbers = array.array('h', [-2, -1, 0, 1, 2])
memv = memoryview(numbers)
len(memv)

memv[0]

memv_oct = memv.cast('B')
memv_oct.tolist()

memv_oct[5] = 4
numbers


