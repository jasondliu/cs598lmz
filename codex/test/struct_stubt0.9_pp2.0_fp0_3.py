from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('b', (1,))
buf = s.pack(42)
s2 = Struct.__new__(Struct)
s2.__init__('b', (1,))
