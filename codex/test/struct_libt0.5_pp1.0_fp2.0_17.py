import _struct
from pypy.rpython.lltypesystem import lltype, llmemory, rffi
from pypy.rpython.lltypesystem.lloperation import llop
from pypy.rpython.memory.gc.base import MovingGCBase
from pypy.rpython.memory.gcheader import GCHeaderBuilder
from pypy.rpython.memory.gcheader import GCFLAG_EXTERNAL
from pypy.rpython.memory.support import (DEFAULT_CHUNK_SIZE,
                                         get_address_of_raw_var_size,
                                         get_address_of_raw_var_item)
from pypy.rpython.memory.support import AddressDict
from pypy.rpython.memory.support import _address_to_int, _int_to_address
from pypy.rpython.memory.support import offset_to_int, int_to_offset
from pypy.rpython.memory.support import get_address_sign_bits, is_64_bit
