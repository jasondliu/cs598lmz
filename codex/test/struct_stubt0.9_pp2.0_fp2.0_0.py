from _struct import Struct
s = Struct.__new__(Struct)
io.BytesIO = BytesIO
s.unpack_from = unpack_from
