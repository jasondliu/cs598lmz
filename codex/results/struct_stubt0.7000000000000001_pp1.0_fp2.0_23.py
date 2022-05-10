from _struct import Struct
s = Struct.__new__(Struct)

s.format = "ii"
s.size = 8

s.pack(123, 456)
#Out[4]: b'{\x00\x00\x00\x7c\x00\x00\x00\x00'
s.pack(123, 456).hex()
#Out[5]: '7b0000007c00000000'

s.unpack(b'{\x00\x00\x00\x7c\x00\x00\x00\x00')
#Out[6]: (123, 456)

s.format = "i"
s.size = 4

s.pack(123)
#Out[7]: b'{\x00\x00\x00'
s.pack(123).hex()
#Out[8]: '7b000000'

s.unpack(b'{\x00\x00\x00')
#Out[9]: (123,)
</code>

