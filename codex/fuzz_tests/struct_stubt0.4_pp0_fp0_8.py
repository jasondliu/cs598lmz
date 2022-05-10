from _struct import Struct
s = Struct.__new__(Struct)
s.format = '<h'
s.size = 2
s.pack(1)

# 以上代码，可以改写成
from _struct import Struct
s = Struct('<h')
s.pack(1)

# 但是，如果没有指定格式，则需要先指定格式
from _struct import Struct
s = Struct()
s.format = '<h'
s.pack(1)

# 因此，Struct类的__new__方法接受一个参数，格式字符串
class Struct(metaclass=StructMeta):
    def __init__(self, fmt):
        self.format = fmt
        self.size = struct.calcsize(fmt)

# 以上代码，可以
