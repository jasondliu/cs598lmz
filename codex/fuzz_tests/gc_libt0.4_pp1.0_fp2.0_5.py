import gc, weakref
from ctypes import *

from pypy.rpython.lltypesystem import lltype, rffi
from pypy.rpython.test.test_llinterp import interpret
from pypy.rpython.lltypesystem.lloperation import llop
from pypy.rpython.lltypesystem import llmemory
from pypy.rpython.memory.gcheader import GCHeaderBuilder
from pypy.rpython.memory.gc.generation import GenerationGC
from pypy.rpython.memory.gc.generation import SemiSpaceGC
from pypy.rpython.memory.gc.generation import MovingGCBase
from pypy.rpython.memory.gc.generation import AddressDict
from pypy.rpython.memory.gc.generation import SemiSpaceAddressDict
from pypy.rpython.memory.gc.generation import GenerationAddressDict
from pypy.rpython.memory.gc.generation import MovingGC
from pypy.rpython.memory.gc.generation import _address_to_int, _int_to_address
from pyp
