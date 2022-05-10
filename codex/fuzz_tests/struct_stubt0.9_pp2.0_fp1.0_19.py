from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('di', 'george')
s.format
s.size
s.pack(1, 2.3)
s.unpack(_)
s.unpack(_)
s.unpack(b'di\x02\x00\x00\x00\x00\x00\x00@\xc3')

# from _struct import unpack
from _struct import unpack
t = unpack('di', 'di\x02\x00\x00\x00\x00\x00\x00@\xc3')
t

# from _struct import unpack_from
from _struct import unpack_from
unpack_from('di', 'di\x02\x00\x00\x00\x00\x00\x00@\xc3', 0)

# from _struct import calcsize
from _struct import calcsize
calcsize('di')

# >>> from _struct import pack_into
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
