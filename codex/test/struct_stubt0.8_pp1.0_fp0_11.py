from _struct import Struct
s = Struct.__new__(Struct)
s.__dict__.update(Struct.__dict__)
s.name, s.format, s.size = 'abc', 'abc', 0
