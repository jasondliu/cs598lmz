from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('bbBHIh')
# TypeError: 'Struct' object is not callable
