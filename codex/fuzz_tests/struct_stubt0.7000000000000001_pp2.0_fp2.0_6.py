from _struct import Struct
s = Struct.__new__(Struct)
s.format = '4s3s'
s.size = s.calcsize(s.format)

class StructField:
    '''Describe a data descriptor that implements storage for s struct field'''
    def __init__(self, format, offset):
        self.format = format
        self.offset = offset
    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            r = struct.unpack_from(self.format, instance._buffer, self.offset)
            return r[0] if len(r) == 1 else r
    def __set__(self, instance, value):
        if not isinstance(value, tuple):
            value = (value,)
        struct.pack_into(self.format, instance._buffer, self.offset, *value)

def StructMeta(clsname, bases, clsdict):
    '''Return a new class that is like cls with added _fields attrs'''
    fields = getattr(cls, '_fields_', [])
   
