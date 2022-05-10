import _struct
#from   struct import pack as struct_pack
#from   struct import unpack as struct_unpack
#from   struct import Struct as struct_struct
#from   _struct import calcsize as struct_calcsize
from   _struct  import unpack  as struct_unpack

#from _struct import Struct as struct_struct
from   _struct import pack    as struct_pack

from sys import byteorder, maxsize
from struct import calcsize, pack, unpack
from math import ceil

from .__logging import get_logger

_L = get_logger(__name__)


def _from_unsigned_short(my_short):
    """
    This is not working as it should...
    """
    #if my_short < 0:
    #    raise RuntimeError("Cannot convert negative to unsigned")
    if my_short > 65535:
        raise RuntimeError("Cannot convert %d to unsigned" % my_short)
    if my_short > 32767:
        my_short -= 65536
    return my_short

