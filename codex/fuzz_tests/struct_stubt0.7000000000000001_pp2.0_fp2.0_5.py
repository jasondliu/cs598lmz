from _struct import Struct
s = Struct.__new__(Struct)
s.format = "&gt;L"
s.size = 4
s.__init__()
s.unpack_from(b'\xcf\x8b\x03\x00')
(7373027L,)
</code>

