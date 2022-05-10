from _struct import Struct
s = Struct.__new__(Struct)
s.__init__("QQQQQQQ", little=True)
s.unpack("A")
s.pack("f" * 13, *range(13))
