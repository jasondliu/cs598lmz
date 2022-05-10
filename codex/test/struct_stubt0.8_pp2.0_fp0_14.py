from _struct import Struct
s = Struct.__new__(Struct)
s.format = ">12s3s4s4s"
s.size = s.calcsize(s.format)
s.unpack("info.txt\x00\x02\x00\x00\x00\x00")
