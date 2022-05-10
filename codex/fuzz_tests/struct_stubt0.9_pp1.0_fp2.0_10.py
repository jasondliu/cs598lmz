from _struct import Struct
s = Struct.__new__(Struct)
s.endianness = '@'
s.size = 18
s.format = 'iif'
compiled_struct = s.__getitem__(slice(18))
