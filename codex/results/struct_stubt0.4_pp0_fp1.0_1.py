from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.unpack(b'\x00\x00\x00\x01')

# 无法创建一个可以处理多个格式的通用的结构体
# 可以使用类似于下面的方法来实现
def unpack_into(fmt, buf, offset=0):
    return Struct(fmt).unpack_from(buf, offset)
unpack_into('>I', b'\x00\x00\x00\x01')

# 对于简单的结构体，可以使用类似下面的方法来实现
import struct
def unpack_into(fmt, buf, offset=0):
    size = struct.calcsize(fmt)
    return
