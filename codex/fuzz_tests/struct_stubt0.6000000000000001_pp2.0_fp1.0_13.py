from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.size

s.pack(1, b'ab', 2.7)

s.unpack(_)

s.unpack_from(bytes, 4)

s.unpack_from(_, 8)

# %%
from array import array
a = array.__new__(array)
a.__init__('b', [1, 2, 3, 4, 5])
a.tolist()

a[0]

a[:]

a[1:3]

a[1:3] = array('b', [7, 8])
a.tolist()

a[1:3] = [7, 8]
a.tolist()

a[1:3] = array('i', [7, 8])
a.tolist()

# %%
from collections import namedtuple
Person = namedtuple('Person', 'name age gender')

bob = Person(name='Bob', age=30, gender='male')

bob[0]


