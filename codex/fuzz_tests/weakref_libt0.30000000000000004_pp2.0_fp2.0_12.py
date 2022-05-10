import weakref

from pypy.rpython.lltypesystem import lltype, llmemory, rffi
from pypy.rpython.lltypesystem.lloperation import llop
from pypy.rpython.memory.gc.base import MovingGCBase
from pypy.rpython.memory.gcheader import GCHeaderBuilder
from pypy.rpython.memory.gcheader import GCFLAG_FORWARDED
from pypy.rpython.memory.gcheader import GCFLAG_HASHTAKEN
from pypy.rpython.memory.gcheader import GCFLAG_TRACK_YOUNG_PTRS
from pypy.rpython.memory.gcheader import GCFLAG_HASHFIELD
from pypy.rpython.memory.gcheader import GCFLAG_HASHFIELD_TYPE
from pypy.rpython.memory.gcheader import GCFLAG_HASHFIELD_VALUE
from pypy.rpython.memory.gcheader import GCFLAG_HASHFIELD_UNUSED
from pypy.rpython.memory.gcheader import GCFLAG_HASHFIELD_UN
