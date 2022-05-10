from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
from _struct import calcsize
calcsize('i')
from _struct import pack, unpack
pack('i', 1)
unpack('i', '\x01\x00\x00\x00')
from _struct import pack_into, unpack_from
from array import array
a = array('i', [1])
pack_into('i', a, 0, 1)
a[0]
unpack_from('i', a, 0)
from _struct import error
from _struct import pack
pack('ii', 1, 2)
from _struct import pack, unpack
pack('ii', 1, 2)
unpack('ii', '\x01\x00\x00\x00\x02\x00\x00\x00')
from _struct import pack_into, unpack_from
from array import array
a = array('i', [1])
pack_into('ii', a, 0, 1, 2)
a
unpack_from('ii', a, 0)
from _struct import pack
