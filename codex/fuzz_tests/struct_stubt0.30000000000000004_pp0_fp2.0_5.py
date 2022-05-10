from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)

# _struct.Struct.pack
# _struct.Struct.unpack

import struct
struct.pack('i', 1)
struct.unpack('i', b'\x01\x00\x00\x00')

# struct.pack
# struct.unpack

# struct.Struct

# struct.Struct.pack
# struct.Struct.unpack

# struct.Struct.__new__
# struct.Struct.__init__

# struct.Struct.format

# struct.Struct.size

# struct.Struct.pack_into
# struct.Struct.unpack_from

# struct.Struct.iter_unpack

# struct.Struct.__repr__

# struct.Struct.__eq__

# struct.Struct.__ne__

# struct.Struct.__hash__

# struct.Struct.__reduce__

# struct.Struct.__reduce_ex__

# struct.Struct.__getnewargs__

# struct.Struct.__
