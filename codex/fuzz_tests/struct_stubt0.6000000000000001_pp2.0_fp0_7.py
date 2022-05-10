from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size
s.pack(1)
s.pack_into(b'',0,1)
s.unpack(b'\x00\x00\x00\x01')
s.unpack_from(b'\x00\x00\x00\x01',0)

#----------------------------------------------------------------------------------------
# The struct module also has these functions:

# struct.calcsize(fmt)
# Return the size in bytes of the struct described by the given format.
# It is useful for calculating the size in bytes of a fixed-size record.

# struct.iter_unpack(fmt, buffer)
# Unpack the buffer according to the format string fmt, returning an iterator that yields a tuple for each format unit in fmt.
# The buffer’s size in bytes must be a multiple of the size of the format unit.

# struct.pack_into(fmt, buffer, offset, v1, v2, ...)
# Pack the values v1, v2, ... according to the format string fmt into the writable buffer buffer starting at
