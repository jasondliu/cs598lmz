from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('16s')
s.unpack(b'Hello\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')

# outputs:
# b'Hello'
