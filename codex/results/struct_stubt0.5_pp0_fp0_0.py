from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.size

# The pack method takes a sequence of values to pack and returns a bytes object containing the packed values
s.pack(1)

# The unpack method takes a bytes object and unpacks the values it contains according to the format string
s.unpack(b'\x00\x00\x00\x01')

# The pack_into and unpack_into methods are similar, but they pack and unpack the values into a pre-existing buffer
buffer = bytearray(b'\x00\x00\x00\x00')
s.pack_into(buffer, 0, 1)
buffer

# The struct module also provides a calcsize function that computes the size of a struct without having to instantiate the Struct object
s.calcsize(b'\x00\x00\x00\x01')

# The struct module provides a number of useful constants, including the sizes in bytes of the built-in C types.
import struct
struct.calcsize('P') * 8

# The format string 'P'
