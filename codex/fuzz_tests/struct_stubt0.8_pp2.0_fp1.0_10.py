from _struct import Struct
s = Struct.__new__(Struct)
s.__init__("B")
s.unpack("\xff")

s = Struct.__new__(Struct)
s.__init__("B")
s.pack(256)

import _struct
s = _struct.Struct("3s")
s.unpack("foo")

s = _struct.Struct("3s")
s.pack("foo")

s = _struct.Struct("x")
s.unpack("a")

s = _struct.Struct("x")
s.pack("a")

s = _struct.Struct("x")
s.unpack("")

s = _struct.Struct("x")
s.pack("")
