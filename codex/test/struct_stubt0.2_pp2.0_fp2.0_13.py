from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.unpack(b'\x01\x00\x00\x00')

# 如果你使用的是 Python 2.7，那么你可以使用一个简单的类来替代上面的代码：
class Struct(object):
    def __init__(self, format):
        self.format = format
    def unpack(self, bytestring):
        return struct.unpack(self.format, bytestring)
    def pack(self, *args):
        return struct.pack(self.format, *args)

# 如果你想使用其他的格式化字符串，那么你可以使用一个元类来实现：
import struct
class Structure(object):
    _fields
