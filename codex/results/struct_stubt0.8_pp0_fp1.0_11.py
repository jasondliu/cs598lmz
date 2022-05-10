from _struct import Struct
s = Struct.__new__(Struct)
s.format = '&lt;3s3sHH'
s.size = 8
print s.unpack(bytearray([0x78,0x59,0x55,0x88,0x66,0x77,0x22,0x00]))
</code>

