from _struct import Struct
s = Struct.__new__(Struct)
s.format = "=hhl"
s.size = s.calcsize(s.format)
s.unpack = s.__call__(s.format)

for i, line in enumerate(open('./data/tiny.txt')):
    data = line.rstrip('\n')
    if i == 0:
        print data
    else:
        l = s.unpack(data)
        print l

import array
a = array.array('l', [1, 2, 3, 4, 5])
print a
print a.itemsize
print a.tolist()

import numpy as np
a = np.array([1, 2, 3, 4, 5])
print a
print a.dtype
print a.size
print a.shape
print a.itemsize
print a[3]
a[3] = 10
print a[3]

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print a
print a.shape

b =
