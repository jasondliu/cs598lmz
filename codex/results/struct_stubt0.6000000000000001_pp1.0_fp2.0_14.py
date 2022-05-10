from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

s.pack(1)

import struct
struct.pack('>H', 1)

import ctypes
ctypes.c_int32(42).value

import array
a = array.array('i', [1,2,3])
a

a.append(4)
a

a.extend([5,6,7])
a

a[1] = 42
a

a.insert(1,2)
a

a.remove(2)
a

a.pop()
a

a.index(2)

a.tolist()

list(a)

a

a.fromlist([1,2,3])
a

a.frombytes(b'\x01\x00\x02\x00\x03\x00')
a

a.tobytes()

a.tostring()

a.tounicode()

a.buffer_info()

a.buffer_info()[1] * a
