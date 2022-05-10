from _struct import Struct
s = Struct.__new__(Struct)
s.__init__("&lt;b")
s.unpack(b"\x00")
</code>

