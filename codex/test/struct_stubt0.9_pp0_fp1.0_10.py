from _struct import Struct
s = Struct.__new__(Struct)
print(s)

print('{} {} {}'.format(s.size, s.pack('hhh', 1, 2, 3), s.unpack('hhh', s.pack('hhh', 1, 2, 3))))

#######################################

from abc import ABCMeta, abstractmethod, abstractproperty
