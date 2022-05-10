from _struct import Struct
s = Struct.__new__(Struct)
s.format = '2i'
s.size = Struct.calcsize(s.format)

class Point(object):
    __slots__ = ['x', 'y']

buffer = create_string_buffer(s.size)

for p in [Point(), Point()]:
    print('{0} {1}'.format(p.x, p.y))
    s.pack_into(buffer, 0, p.x, p.y)
    print(s.unpack_from(buffer, 0))
</code>

