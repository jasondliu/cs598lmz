from _struct import Struct
s = Struct.__new__(Struct)
s.format = ">B"
s.size = 1
s.pack = lambda x : x.to_bytes(1, byteorder = "big")
