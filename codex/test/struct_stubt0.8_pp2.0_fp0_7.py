from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)

# TypeError: Struct() argument 1 must be string, not unicode
#s = Struct()
#s.__init__(u'i')
#s.pack(1)

# TypeError: expected string without null bytes
s = Struct.__new__(Struct)
s.__init__('i\0')
s.pack(1)
