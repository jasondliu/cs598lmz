from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('x')
s.unpack_from(b'x', 0)
s.unpack_from(b'x', 0)

# __init__() returns None, so make sure it doesn't crash
assert s.unpack_from(b'x', 0) == (b'x',)

# noinspection PyUnresolvedReferences
s = Struct.__new__(Struct)
s.__init__('x')
s.unpack_from(b'x', 0)
s.unpack_from(b'x', 0)

assert s.unpack_from(b'x', 0) == (b'x',)

s.pack_into(b'x', 0, b'x')

s = Struct.__new__(Struct)
s.__init__('x')
s.pack_into(b'', 0, b'x')
s.pack_into(b'', 0, b'x')

assert s.pack_into(b'', 0, b'x') == None

s = Struct.
