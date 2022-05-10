import gc, weakref
from pypy.rpython.lltypesystem import lltype, llmemory, rffi
from pypy.rpython.lltypesystem.lloperation import llop
from pypy.rpython.memory.support import get_address_stack, get_address_deque
from pypy.rpython.memory.support import DEFAULT_CHUNK_SIZE
from pypy.rpython.memory.support import AddressDict
from pypy.rpython.memory.gc.base import MovingGCBase
from pypy.rpython.memory.gcheader import GCHeaderBuilder
from pypy.rpython.memory.gcheader import GCFLAG_FORWARDED
from pypy.rpython.memory.gcheader import GCFLAG_HASHTAKEN
from pypy.rpython.memory.gcheader import GCFLAG_EXTERNAL
from pypy.rpython.memory.gcheader import GCFLAG_NO_HEAP_PTRS
from pypy.rpython.memory.gcheader import GCFLAG_NO_YOUNG_PTRS
from pypy
