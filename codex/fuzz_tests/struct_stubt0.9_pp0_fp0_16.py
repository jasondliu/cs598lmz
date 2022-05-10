from _struct import Struct
s = Struct.__new__(Struct)
print(s.pack(b'hhl', 1, 2, 3))
# b'\x01\x00\x02\x00\x00\x00\x03\x00\x00\x00'
</code>

