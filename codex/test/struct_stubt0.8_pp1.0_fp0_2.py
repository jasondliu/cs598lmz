from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i2shi')
s.size
s.pack(1, b'xy', 2, b'z')
s.unpack(_)
s.unpack_from(b'\x01\x00\x00\x00xy\x02\x00\x00\x00z', 0)

import sys
sys.getsizeof(1)
import array
sys.getsizeof(array.array('c', 'x' * 1000))

