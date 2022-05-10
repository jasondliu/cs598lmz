from _struct import Struct
s = Struct.__new__(Struct) # use a new instance of the struct type
s.__init__('i') # initialize the struct with a format string
s.unpack(b'\x00\x00\x00\x0a') # unpack a 4-byte string into an int
(10,)

s.pack(10) # pack an int into a 4-byte string
b'\x00\x00\x00\n'

s.unpack(b'\x00\x00\x01\x00') # unpack a 4-byte string into an int
(256,)

s.pack(256) # pack an int into a 4-byte string
b'\x00\x00\x01\x00'

# use the new Struct instance to unpack the byte string
s.unpack(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
(0, 0, 0, 0, 0, 0, 0, 0)

# use the new Struct instance to pack the
