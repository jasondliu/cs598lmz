from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'i'
s.size = 4
s.pack(1)

# 使用__new__方法创建类
class StructureMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        fields = getattr(cls, '_fields_', [])
        byte_order = ''
        offset = 0
        for format, fieldname in fields:
            if isinstance(format, StructureMeta):
                setattr(cls, fieldname, NestedStruct(format, offset))
                offset += format.size
            else:
                if format.startswith(('<', '>', '!', '@')):
                    byte_order = format[0]
                    format = format[1:]
                format = byte_order + format
                setattr(cls, fieldname, StructField(format, offset))
