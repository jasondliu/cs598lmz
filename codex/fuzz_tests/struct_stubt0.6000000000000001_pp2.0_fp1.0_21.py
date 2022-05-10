from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.unpack(b'\xFF\xFF\xFF\xFF')

# struct.error: unpack requires a buffer of 4 bytes
</code>

