from _struct import Struct
s = Struct.__new__(Struct)
s.format = b'I'
s.size = 4
s.pack = Struct.__dict__['pack']
s.unpack = Struct.__dict__['unpack']
s.pack(1)
