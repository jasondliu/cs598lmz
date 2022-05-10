from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'fi'
l = s.unpack('3.1415\x00\x01\x00\x00')
# (3.1415, 1.0)
s.format = 'ff'
s.unpack('3.1415\x00\x01\x00\x00')
# (3.1415, 1.0)

s = Struct.__new__(Struct)
s.format = '1.1f'
l = s.unpack('1\x00')
# (1.0,)
s.format = 'i'
l = s.unpack('\x01')
# (1,)
</code>

