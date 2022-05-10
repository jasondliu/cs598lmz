from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.size

# 打包
data = s.pack(1, b'ab', 2.7)

# 解包
s.unpack(data)

# 封装成类
class StructField:
    '''
    Descriptor representing a simple structure field
    '''

    def __init__(self, format, offset):
        self.format = format
        self.offset = offset

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            r = struct.unpack_from(self.format, instance._buffer, self.offset)
            return r[0] if len(r) == 1 else r

class Structure:
    '''
    Basic structure with initializer
    '''
    def __init__(self, bytedata):
        self._buffer = memoryview(bytedata)

class PolyHeader(Structure):
    file_code = StructField('<i', 0
