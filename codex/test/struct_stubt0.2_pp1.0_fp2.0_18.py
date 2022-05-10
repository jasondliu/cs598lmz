from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>i')
s.unpack(b'\x00\x00\x00\x01')

# 如果你的目的只是简单的打包和解包，那么使用上面的代码就已经足够了。
# 但是，如果你想将你的结构体定义成一个类的话，那么你可以像下面这样写：

from _struct import Struct

class StructField:
    '''
    Descriptor representing a simple structure field
    '''
    def __init__(self, format, offset):
        self.format = format
        self.offset = offset
