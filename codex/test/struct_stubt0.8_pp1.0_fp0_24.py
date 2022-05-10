from _struct import Struct
s = Struct.__new__(Struct)
s.__init__(s, 'hi')
s.pack(1,2)
