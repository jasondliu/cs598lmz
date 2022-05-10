from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>i')
s.size

# 这个构造方法通常是用来实现类方法的，比如：
import math
class StructureMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        clsobj = super().__new__(cls, clsname, bases, clsdict)
        fields = getattr(clsobj, '_fields_', [])
        byte_order = ''
        offset = 0
        for format, fieldname in fields:
            if isinstance(format, StructureMeta):
                setattr(clsobj, fieldname, property(lambda self: self._buffer))
                continue
            format = byte_order + format
            setattr(clsobj, fieldname, property(
                    fget=lambda self, format=format, offset=offset:
                    self._unpack_field(format, offset)))
