from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i?f')
s.size

s.pack(1, False, 3.14159)

s.unpack(_)

s.unpack_from(buffer(a), 0)

s.unpack_from(buffer(a), 4)

s = Struct('i?f')
s.pack(1, False, 3.14159)

s.unpack(_)

s.unpack_from(buffer(a), 0)

s.unpack_from(buffer(a), 4)

a = array('i', xrange(5))
a

a.tostring()

a.tostring() == buffer(a)

a.fromstring(a.tostring())

a

a.fromstring('spam')

a

a.fromstring('spamspam')

a

a.fromstring('spamspamspam')

a

a = array('i', xrange(5))
a

