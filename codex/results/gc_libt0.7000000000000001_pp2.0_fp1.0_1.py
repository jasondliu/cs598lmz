import gc, weakref, sys

from weakref import WeakValueDictionary

from pypy.rpython.lltypesystem import lltype, llmemory, llarena
from pypy.rpython.lltypesystem.lloperation import llop
from pypy.rpython.lltypesystem.rstr import STR, mallocstr
from pypy.rpython.lltypesystem.rstr import copystrcontent
from pypy.rpython.lltypesystem.rstr import copystrcontent_nocheck
from pypy.rpython.memory.gctransform import asmgcroot, shadowstack_gcroot
from pypy.rpython.lltypesystem.llmemory import raw_malloc_usage, raw_free_usage
from pypy.rpython import rclass
from pypy.rpython.memory.support import get_address_stack, get_address_deque
from pypy.rpython.memory.support import get_address_list, AddressDict
from pypy.rpython.memory.support import get_address_set, AddressKeyError
from pypy
