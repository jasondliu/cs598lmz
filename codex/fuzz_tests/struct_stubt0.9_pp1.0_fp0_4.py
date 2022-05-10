from _struct import Struct
s = Struct.__new__(Struct)
s.__init__("Bh")
s.pack(0x00, 0x00, 0x0FAC)
</code>
This seems to work well, but I'll never do it again.

