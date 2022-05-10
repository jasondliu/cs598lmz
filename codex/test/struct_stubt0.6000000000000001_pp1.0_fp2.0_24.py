from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('<l')
s.size

import struct
struct.calcsize('<l')

import array
a = array.array('l')
a

a.append(23)
a

a.append(45)
a

a.append(67)
a

a[1]

a[-1]

a.extend([45,67,89])
a

a.insert(1,100)
a

a.remove(45)
a

a.pop()
a

a.pop(2)
a

a.index(67)

a.reverse()
a

a.tolist()

a.tostring()


a.fromlist([1,2,3])
a

a.fromstring('abcd')
a

a.tofile(open('test.bin', 'wb'))

a.fromfile(open('test.bin', 'rb'), 4)
a

