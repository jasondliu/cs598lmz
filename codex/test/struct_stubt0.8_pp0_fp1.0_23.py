from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')

# Now:
s.pack_into(buf, 0, 0x1234567)
