from _struct import Struct
s = Struct.__new__(Struct)
s.__init__(Struct, "s" )
s.unpack( s.pack("jaslkdf") )
