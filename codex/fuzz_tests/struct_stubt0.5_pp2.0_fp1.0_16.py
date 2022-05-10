from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('<i')
s.unpack_from(b'\x00\x00\x00\x01', 0)

# from _struct import Struct
# s = Struct.__new__(Struct)
# s._fmt = '<i'
# s._fmt_check(s._fmt)
# s._pack(1)
# s._unpack(b'\x00\x00\x00\x01', 0)

# from _struct import Struct
# s = Struct.__new__(Struct)
# s._fmt = '<i'
# s._fmt_check(s._fmt)
# s._pack(1)
# s._unpack(b'\x00\x00\x00\x01', 0)

# from _struct import Struct
# s = Struct.__new__(Struct)
# s._fmt = '<i'
# s._fmt_check(s._fmt)
# s._pack(1)
# s._unpack(b'\x00\
