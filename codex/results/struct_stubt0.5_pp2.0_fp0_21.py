from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'H'
s.size = 2
s.pack(1)

# Explicitly calling __new__()
class SubStruct(Struct):
    def __new__(cls, *args):
        return Struct.__new__(cls, *args)

# Example:
from _struct import Struct

class SubStruct(Struct):
    def __new__(cls, *args):
        return Struct.__new__(cls, *args)

    def __init__(self, *args):
        super(SubStruct, self).__init__(*args)
        self.value = args[0]

    def __repr__(self):
        return 'SubStruct(%s)' % self.value

s = SubStruct('H')
s
# SubStruct(H)
s.size
# 2
s.pack(1)
# b'\x01\x00'

# __new__() and __init__()
class Date(object):
    def __init__(self, year, month, day):
        self.year
