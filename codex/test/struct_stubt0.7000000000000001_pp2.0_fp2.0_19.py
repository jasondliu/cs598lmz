from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>1s1s1s1s', '>')
s.pack(b'A', b'B', b'C', b'D')

