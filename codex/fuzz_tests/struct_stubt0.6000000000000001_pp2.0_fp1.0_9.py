from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')

print(s.size)  # 4
print(s.pack(1))  # b'\x01\x00\x00\x00'
print(s.unpack(b'\x01\x00\x00\x00'))  # (1,)
</code>

