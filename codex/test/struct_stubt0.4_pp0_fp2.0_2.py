from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.unpack(b'\x00\x00\x00\x00')

# b'\x00\x00\x00\x00' is a bytes object, which is iterable over integers
# (the bytes). So this is equivalent to:
s.unpack(iter(b'\x00\x00\x00\x00'))
