from _struct import Struct
s = Struct.__new__(Struct)
s.__dict__.update(Struct._FIELDS)
