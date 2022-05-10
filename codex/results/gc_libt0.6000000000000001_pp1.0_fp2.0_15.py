import gc, weakref, os
from pypy.rpython.lltypesystem import lltype, rffi
from pypy.rpython.lltypesystem.lloperation import llop
from pypy.rpython.lltypesystem.llmemory import GCREF
from pypy.rpython.lltypesystem.llmemory import raw_malloc_usage, raw_memcopy
from pypy.rpython.memory.gc.base import MovingGCBase
from pypy.rpython.memory.gcheader import GCHeaderBuilder
from pypy.rpython.memory.gcheader import sizeofaddr, sizeofaddr_signed
from pypy.rpython.memory.gcheader import mark_gc_roots, mark_as_root
from pypy.rpython.memory.support import get_address_stack, get_address_deque
from pypy.rpython.memory.support import AddressDict
from pypy.rpython.memory.support import get_address_of_null_object, NULL
from pypy.rpython.memory.support import get_address_of_stack_bottom

