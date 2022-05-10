from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i?f')
s.size
s.pack(1, False, 3.14159)
s.unpack(_)
s.unpack(_)
s.unpack(_)
 
from struct import Struct
s = Struct('i?f')
s.pack(1, False, 3.14159)
s.unpack(_)
s.unpack(_)
s.unpack(_)
 
s = Struct('i?f')
s.pack(1, False, 3.14159)
s.unpack(_)
s.unpack(_)
s.unpack(_)
 
from struct import Struct
from time import localtime
 
now = localtime()
