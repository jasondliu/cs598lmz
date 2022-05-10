from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('hhl')
s.size

s = Struct('hhl')
s.size

import sys
s = Struct('i')
sys.getsizeof(s)


s = Struct('i')
t = Struct('i')
s is t

s = Struct('i')
t = Struct('l')
s is t

s = Struct('i')
t = Struct('i')
hash(s) == hash(t)

s = Struct('i')
t = Struct('l')
hash(s) == hash(t)

s = Struct('P')
t = Struct('P')
hash(s) == hash(t)


Struct('hhh')
Struct('hhi')

Struct('hhh')
Struct('hh')

s = Struct('hhh')
s.format

s = Struct('hhh')
s.unpack(b'\x01\x02\x03')

s = Struct('hhh')
s.unpack(b'\x01\x02\x03\x04')

s = Struct
