from _struct import Struct
s = Struct.__new__(Struct)
#s._update_format_string
s.format = 'I'
s.size = 4
s.pack(1)

