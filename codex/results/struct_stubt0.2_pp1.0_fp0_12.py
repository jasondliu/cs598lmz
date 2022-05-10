from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)

# 可以使用__new__方法来创建不可变的类
class StructureMeta(type):
    '''
    元类，用于创建一个结构体类
    '''
    def __init__(self, clsname, bases, clsdict):
        fields = getattr(self, '_fields_', [])
        byte_order = ''
        offset = 0
        for format, fieldname in fields:
            if isinstance(format, StructureMeta):
                setattr(self, fieldname, NestedStruct(format, offset))
                offset += format.struct_size
            else:
                if format.startswith(('<', '>', '!', '@')):
                    byte_order = format[0]
                    format = format[1:]
                format = byte_order + format
                setattr(self, fieldname
