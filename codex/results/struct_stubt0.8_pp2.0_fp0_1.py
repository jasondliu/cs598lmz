from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('hhl')
# struct.pack is an explicit way to do that.
# struct.unpack works in the same way, but goes in the opposite direction.

# The other way to use struct is as a context manager
with open('somefile', 'rb') as f:
    data = f.read(16)
    print(data)
    unpacked_data = struct.unpack('iif', data)
    print(unpacked_data)

# You can then use this data to create named tuples
from collections import namedtuple
Record = namedtuple('Record', ['kind', 'x', 'y'])
with open('data.b', 'rb') as f:
    records = (Record(*r) for r in zip(*[iter(f.read())] * calcsize('iif')))
    for r in records:
        print(r.kind, r.x, r.y)

# If you are only dealing with a single structure, you may simply use
# the _make() method of a namedtuple.
with open('data.
