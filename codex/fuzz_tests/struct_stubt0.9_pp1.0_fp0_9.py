from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('bb')
s.size
s.pack(1,2)
b = bytes(s.pack(1,2))
b
s.unpack(b)
s.unpack_from(b)
m = memoryview(b)
s.unpack_from(m)
m2 = m[:2]
m2
s.unpack_from(m2)
%%file arraydemo.py
from array import array
from random import random
floats = array('d', (random() for i in range(10**7)))
floats[-1]
fp = open('/tmp/floats.txt', 'wb')
floats.tofile(fp)
fp.close()
floats2 = array('d')
fp = open('/tmp/floats.txt', 'rb')
floats2.fromfile(fp, 10**7)
fp.close()
floats2[-1]
floats2 == floats

%%file arraydemo2.py
from array import array
from random import random

floats = array
