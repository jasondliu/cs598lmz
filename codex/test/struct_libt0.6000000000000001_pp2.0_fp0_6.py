import _struct
import sys
import traceback

from . import _util, _constants
from . import _cs_struct

if sys.version_info < (3, 0):
    integer_types = (int, long)
else:
    integer_types = (int,)


class _Struct(object):
    """A class that can be used to create packed C structures.

    The resulting class is subclassable, and its constructor
    takes the same parameters as the struct.pack() function.
    """

    def __init__(self, format, *args):
        self.format = format
        self.size = struct.calcsize(format)
        self.__dict__["cs"] = _cs_struct.Struct(format)
        self.pack(*args)

    def pack(self, *args):
        self.__dict__["buffer"] = self.cs.pack(*args)

    def pack_into(self, buf, offset, *args):
        self.cs.pack_into(buf, offset, *args)

