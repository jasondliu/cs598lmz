from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.size

# 在类中定义元类
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
                setattr(self, fieldname, Struct(format))
                offset += getattr(self, fieldname).size
        setattr(self, 'struct_size', offset)

