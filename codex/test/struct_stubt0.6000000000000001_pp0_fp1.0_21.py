from _struct import Struct
s = Struct.__new__(Struct)
s.size = 3
s.format = "<BHH"
s.pack_into(bytearray(10), 0, 0, 1, 2)

# This should fail with:
# TypeError: 'bytes' does not support the buffer interface
s.pack_into(str(bytearray(10)), 0, 0, 1, 2)
