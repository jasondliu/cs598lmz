from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.size

s.pack(1, 'ab', 3.0)

s.unpack(_)

s.unpack_from(buffer('\x01\x00\x00\x00ab\x00\x00\x00@'), 0)

s.unpack_from(buffer('\x01\x00\x00\x00ab\x00\x00\x00@'), 4)

import array
a = array.array('c', 'hello world')
a

a.tostring()

a.fromstring('howdy')

a

a.tostring()

a.fromstring('d\x00\x00w\x00y\x00')

a

a.tostring()

a.fromstring('d\x00\x00w\x00y\x00')

a.tostring()

a.fromstring('d\x00\x00w\x00y\x00')

a.tost
