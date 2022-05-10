from _struct import Struct
s = Struct.__new__(Struct)
s.size = Struct.Size(s)
s.format = Struct.Format(s)
s.pack = Struct.Pack(s)
s.unpack = Struct.Unpack(s)
s.unpack_from = Struct.UnpackFrom(s)
