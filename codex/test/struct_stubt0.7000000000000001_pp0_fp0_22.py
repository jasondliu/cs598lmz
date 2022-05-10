from _struct import Struct
s = Struct.__new__(Struct)
s.__setattr__("format", "HhL")
s.__setattr__("size", 8)
