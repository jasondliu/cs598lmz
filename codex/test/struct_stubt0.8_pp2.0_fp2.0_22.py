from _struct import Struct
s = Struct.__new__(Struct)
s.__dict__ = Struct.__dict__
s

