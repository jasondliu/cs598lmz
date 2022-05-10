from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'i'
s.size = 4
s.pack(42)

import struct
struct.pack('i', 42)

import array
a = array.array('i', [1, 2, 3])
a

a.append(4)
a

a.extend([5, 6, 7])
a

a.insert(1, 42)
a

a.pop()
a

a.remove(42)
a

a.reverse()
a

a.tolist()

a.count(2)

a.index(2)

a.buffer_info()

a.buffer_info()[1] * a.itemsize

a.typecode

a.itemsize

a.byteswap()

a.byteswap()

a.count(2)

a.index(2)

a.tolist()

a.tobytes()
