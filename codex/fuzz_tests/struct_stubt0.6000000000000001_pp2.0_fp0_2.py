from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'I'
s.size = 4
import array
values = [1, 2, 3]
a = array.array('I', values)
print(len(a))
print(a)

import binascii
data = s.pack(*values)
print(len(data))
print(binascii.hexlify(data))

print(s.unpack(data))

print(a.tobytes())

bytes_array = a.tobytes()
print(s.unpack_from(bytes_array, 0))
print(s.unpack_from(bytes_array, s.size))
