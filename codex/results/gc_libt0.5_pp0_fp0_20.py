import gc, weakref

import py
from pypy.rlib.debug import fatalerror
from pypy.rpython.lltypesystem import lltype, llmemory, rclass, rstr
from pypy.rpython.lltypesystem.lloperation import llop
from pypy.rpython.memory.gc.base import MovingGCBase
from pypy.rpython.memory.gc.base import choose_gc_from_config
from pypy.rpython.memory.gcheader import GCHeaderBuilder
from pypy.rpython.memory.support import get_address_stack, get_address_deque
from pypy.rpython.memory.support import get_address_link, get_address_field
from pypy.rpython.memory.support import DEFAULT_CHUNK_SIZE, DEFAULT_ARRAY_SIZE
from pypy.rpython.memory.support import get_address_of_gc_object, get_address_of_non_gc_object
from pypy.rpython.memory.support import get_rpy_roots
from pypy.
