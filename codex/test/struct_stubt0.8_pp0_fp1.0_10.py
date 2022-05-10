from _struct import Struct
s = Struct.__new__(Struct) # zero-length struct
s.unpack("") # no error
