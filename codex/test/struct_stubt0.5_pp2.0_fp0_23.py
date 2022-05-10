from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.size

# 这种方式创建的类和直接使用class语句创建的类没有什么区别，因为Python会在内部调用type来创建Struct类
# Struct = type('Struct', (object,), {'__init__': __init__, 'pack': pack, 'unpack': unpack, 'size': size})

# 为了让Struct实例支持属性引用，可以使用__slots__属性
def __init__(self, format, endianness='>'):
    self._format = endianness + format
    self._size = struct.calcsize(self._format)

