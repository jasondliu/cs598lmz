from _struct import Struct
s = Struct.__new__(Struct)
s.format = '4s4s'
s.size = s.calcsize(s.format)
print(s.unpack(b'\x01\x02\x03\x04\x05\x06\x07\x08'))

# 对于不同的结构，我们可以定义出不同的子类
class StructField:
    def __init__(self, format, offset):
        self.format = format
        self.offset = offset
    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            r = struct.unpack_from(self.format, instance._buffer, self.offset)
            return r[0] if len(r) == 1 else r

class NestedStruct:
    def __init__(self, name, struct_type, offset):
        self.name = name
        self.struct_type = struct_type
        self.offset = offset
