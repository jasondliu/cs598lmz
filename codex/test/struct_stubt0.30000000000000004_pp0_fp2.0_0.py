from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>i')
s.unpack(b'\x00\x00\x00\x01')

# 如果你的目的只是简单的打包和解包，你可以使用更加简单的 struct 模块中的 pack() 和 unpack() 函数。
# 下面是一个简单的例子：
import struct
data = struct.pack('>i4sh', 7, b'spam', 8)
data
struct.unpack('>i4sh', data)

# 当打包的时候，你需要提供一个格式字符串作为第一个参数。这个字符串中的每个
