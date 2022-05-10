from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('<h')
s.pack(-1)

import _struct
import struct

_struct.pack('<h', -1)
struct.pack('<h', -1)


