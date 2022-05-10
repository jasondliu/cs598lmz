from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'i?xx'
s.size = s.calcsize()
s.data = 'aaaa'
s.unpack(s.data)
s.unpack_from(s.data)
s.pack(1, True)
s.pack_into(s.data, 0, 1, True)

import _struct
_struct.__dict__.keys()

# test __dir__
import _struct
dir(_struct)
dir(_struct.Struct(''))

# This tests the name mangling used by _struct
# as well as some otherwise unreachable code
# in standardobject.c, used (indirectly) by Struct.format
assert _struct._clearcache.__name__ == '_struct._clearcache'
assert _struct._Struct._Struct.__name__ == '_struct._Struct'

class TestUnsignedBug:
    """
    Test case for SF bug #1435795
    """
    def __init__(self):
        self.unpack = Struct('L').unpack

    def byteswap(self, word
