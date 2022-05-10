from _struct import Struct
s = Struct.__new__(Struct)
s.size = Struct.size
s.pack = Struct.pack
s.unpack = Struct.unpack
