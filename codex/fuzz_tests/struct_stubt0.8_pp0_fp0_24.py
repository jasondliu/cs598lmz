from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I2sf')
s.size

s = Struct('I2sf')
s.size

s = Struct('I2sf')
s.pack(b'abc', 42, 3.14, 999)

s = Struct('I2sf')
values = (b'abc', 42, 3.14, 999)
s.pack(*values)
s.unpack(_)

s = Struct('I2sf')
template = ''.join('{}{:d}s'.format(t, n) for t, n in s.iter_unpack())
template

s = Struct('I2sf')
template = ''.join('{}{:d}s'.format(t, n) for t, n in s.iter_unpack())
values = (b'abc', 42, 3.14, 999)
for v in zip(template, values):
    print('{:6} -> {}'.format(*v))


from _struct import calcsize
calcsize('P2I2f')

from _struct import pack
pack('P2
