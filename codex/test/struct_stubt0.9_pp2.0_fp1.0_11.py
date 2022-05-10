from _struct import Struct
s = Struct.__new__(Struct)
# See docs for {Struct}_format for flags and their meaning
s.__init__('''b  t c l  h i l ll'''
           '''q iq f d  x s p''')
s.size = s.size # print size of structure
# len(s.pack(*s)) == s.size == s.calcsize()
s
s.pack(-1, 0, 1, -2, 3, 4, -5, 6, 7, -8, -9, 10.1, 11.2, '', 'a')
s.pack_into(buf, offset, *s)
s.unpack(buf[offset:offset+s.size])
s.unpack_from(buf, offset)
print('*'*70) ; print('Automatically use struct.Struct(\'Qf\')...')
print('*'*70) ; sys.stdout.flush()
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('Qf')
s.size = s.size # print size of structure

