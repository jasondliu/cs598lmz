from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('2i 3h', False)
s.size

