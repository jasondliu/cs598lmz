from _struct import Struct
s = Struct.__new__(Struct)
s.format = '<pkn'
import array
data = array.array('b', '\x00V\xbe\x1c\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00p')
fields = s.unpack_from(buffer(data))
print fields
