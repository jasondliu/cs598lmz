from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('<h')
s.unpack(b'\x00\x01')

# struct.unpack_from()
from struct import unpack_from
unpack_from('<h', b'\x00\x01')

# struct.pack_into()
from struct import pack_into
pack_into('<h', b'\x00\x00\x00\x00', 0, 1)

# struct.calcsize()
from struct import calcsize
calcsize('<h')

# struct.iter_unpack()
from struct import iter_unpack
list(iter_unpack('<h', b'\x00\x01\x00\x02'))

# struct.Struct()
from struct import Struct
Struct('<h')

# struct.error
from struct import error

# struct.pack()
from struct import pack
pack('<h', 1)

# struct.unpack()
from struct import unpack
unpack('<h', b'\x00\x01')

#
