from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# test packing and unpacking
x = s.pack(42)
x
s.unpack(x)

# test that __new__ is called with the correct arguments
class SubStruct(Struct):
    def __new__(cls, format, *args):
        return Struct.__new__(cls, 'hhl' + format)

SubStruct('i')

# test that __new__ is called with the correct arguments
class SubStruct(Struct):
    def __new__(cls, format, *args):
        return Struct.__new__(cls, 'hhl' + format, *args)

SubStruct('i')

# test that __init__ is called with the correct arguments
class SubStruct(Struct):
    def __init__(self, format, *args):
        Struct.__init__(self, 'hhl' + format, *args)

SubStruct('i')

# test that __init__ is called with the correct arguments
class SubStruct(Struct):
    def __init
