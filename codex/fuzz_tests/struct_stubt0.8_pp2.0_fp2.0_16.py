from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('bbhhl', 0, 0, 0, 0, 0, 0)
s.size = s.size
s.pack(1, 2, 3, 4, 5)
s.unpack(s.pack(1, 2, 3, 4, 5))


import _struct
_struct.error
_struct.pack
_struct.unpack

import _struct as s
s.error
s.pack
s.unpack

from _struct import error
from _struct import pack
from _struct import unpack

error
pack
unpack

from _struct import *
error
pack
unpack


# These are used by the _test() function
from _struct import _clearcache
from _struct import _islittle
from _struct import _sys_byteorder
from _struct import calcsize
from _struct import pack
from _struct import unpack


# Tests a function that should be renamed
from _struct import _struct as struct
struct()

# Tests a method that should be renamed
from _struct import _struct as struct
struct().pack()
