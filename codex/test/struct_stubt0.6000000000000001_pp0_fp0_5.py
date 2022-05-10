from _struct import Struct
s = Struct.__new__(Struct)
s.__setattr__('format', 'i')
s.unpack(b'\xf0\x00\x00\x00')

# 方法三
from _struct import _clearcache
_clearcache()
from _struct import Struct
s = Struct.__new__(Struct)
s.__setattr__('format', 'i')
s.unpack(b'\xf0\x00\x00\x00')

# 方法四
from _struct import _clearcache
_clearcache()
from _struct import Struct
s = Struct.__new__(Struct)
s.__setattr__('format', 'i')
s.unpack(b'\xf0\x00\x00\x00')

# 方法五
from _struct import _clearcache
_clearcache()
from _struct import Struct
s = Struct.__new__(Struct)
s.__setattr__('format', 'i')
