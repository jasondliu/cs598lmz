from _struct import Struct
s = Struct.__new__(Struct)
s.format = '<2i'
s.size = 8
s.pack(1,2)

# _struct.Struct.__new__(_struct.Struct)

# _struct.Struct.__new__.__globals__['_struct'].Struct

# _struct.Struct.__new__.__globals__['_struct']

# _struct.Struct.__new__.__globals__
