from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>i')
s.size

# 可以使用给定的格式字符串创建一个新的结构体类，然后实例化后调用pack()或unpack()方法。
# 但是，通常更简单的方式是使用一个工厂函数来创建这个类，比如
import struct
def unpack_int(data):
    return struct.unpack('>i', data)

# 可以使用struct.Struct类来定义一个结构体，然后使用pack()和unpack()方法来打包和解包。
#
