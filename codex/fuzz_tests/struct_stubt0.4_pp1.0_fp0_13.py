from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.pack(1, 'ab'.encode('utf-8'), 2.7)

# '\x01\x00\x00\x00ab\x00\x00\x9a\x99\x99\x99\x99\x9a'

s.unpack(_)

# (1, b'ab', 2.700000047683716)

s.size

# 12

# The struct module is a powerful part of the standard library, but it is not the only option.
# An alternative is the array module, which provides the array type.
# The array type is just like a list that stores only homogeneous data and stores it more compactly.
# To create an array, give the typecode and an iterable containing initial values:

from array import array
a = array('I', (1, 2, 3))

# array('I', [1, 2, 3])

a

# array('I', [1, 2, 3])

a.append(4)
a

