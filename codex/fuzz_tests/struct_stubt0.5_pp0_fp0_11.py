from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'i'
s.size = 4
s.pack(1)

# numpy
from numpy import array
a = array([1, 2, 3], dtype='i')
a.tobytes()

# array
from array import array
a = array('i', [1, 2, 3])
a.tobytes()

# memoryview
m = memoryview(b'\x01\x02\x03')
m.tobytes()

# bytearray
b = bytearray(b'\x01\x02\x03')
b.tobytes()

# bytes
b = b'\x01\x02\x03'
b

# ctypes
from ctypes import c_int
c_int(1).value

# dbm
import dbm
db = dbm.open('/tmp/example.db', 'c')
db[b'key'] = b'value'
b'key' in db
db[b'key']
db.close()

# sqlite3
