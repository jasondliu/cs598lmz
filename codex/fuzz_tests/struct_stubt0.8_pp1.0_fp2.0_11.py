from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.pack(1, 'ab'.encode('utf-8'), 2.7)

# just a normal callable class
class MyStruct:
    def __init__(self, format):
        self.format = format

    def pack(self, *args):
        return struct.pack(self.format, *args)

    def unpack(self, *args):
        return struct.unpack(self.format, *args)

    def calcsize(self, *args):
        return struct.calcsize(self.format)

s = MyStruct('I 2s f')
s.pack(1, 'ab'.encode('utf-8'), 2.7)

# Metaclass Approach
class StructureMeta(type):

    def __init__(self, clsname, bases, clsdict):
        fields = getattr(self, '_fields_', [])
        byte_order = ''
        offset = 0
        for format, fieldname in fields:
            if isinstance(format, StructureMeta):
