from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>i')
s.unpack(b'\x00\x00\x00\x00')

# This is the same as:

from _struct import Struct
Struct('>i').unpack(b'\x00\x00\x00\x00')

# The first example is more verbose, but it is more flexible.
# It allows you to reuse the Struct object and unpack multiple values.

# The Struct class has a pack() method that takes an iterable of values
# and packs them into a bytes object.

from _struct import Struct
s = Struct('>i')
s.pack(1)

# The Struct class also has a calcsize() method that returns the size
# of the struct in bytes.

from _struct import Struct
s = Struct('>i')
s.calcsize()

# The Struct class also has a pack_into() method that accepts a buffer
# as the first argument.

from _struct import Struct
s = Struct('>i')
buffer = bytearray(s.size)
