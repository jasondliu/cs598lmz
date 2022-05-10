from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>i')
s.size

# 使用类方法
Struct.__new__(Struct, '>i')

# 使用元类
Struct('>i')

# 使用元类
class StructureMeta(type):
    def __init__(self, clsname, bases, clsdict):
        fields = getattr(self, '_fields_', [])
        byte_order = ''
        offset = 0
        for format, fieldname in fields:
            if isinstance(format, StructureMeta):
                setattr(self, fieldname, NestedStruct(format, offset))
                offset += format.size
            else:
                if format.startswith(('<', '>', '!', '@')):
                    byte_order = format[0]
                    format = format[1:]
                format = byte_order + format
                setattr(self, fieldname, Struct(format).unpack_from)
                offset += Struct(format).size
        setattr
