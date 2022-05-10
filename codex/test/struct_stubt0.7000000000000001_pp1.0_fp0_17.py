from _struct import Struct
s = Struct.__new__(Struct)
s.__setattr__('format', 'I 2s f')
s.size = s.__sizeof__()

print(f'{s.size=}')

import array
f = open('data.bin', 'rb')
a = array.array('u', b'abcdefg')
print(a.itemsize)

import os
print(os.stat('data.bin'))
print(os.stat('data.bin').st_size)
