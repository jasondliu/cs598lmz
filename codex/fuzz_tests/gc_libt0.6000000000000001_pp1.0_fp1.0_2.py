import gc, weakref, os, sys

from pypy.rpython.memory.support import RawBuffer, NULL
from pypy.rpython.memory.gc.base import MovingGCBase, GCBase
from pypy.rpython.lltypesystem.lltype import (malloc, free,
    cast_pointer, offsetof, typeOf, malloc_nonmovable,
    sizeof, getRuntimeTypeInfo, nullptr, is_null_ptr,
    typeOf, TypeOf, get_function_type, get_array_type)
from pypy.rpython.memory.gcheader import GCHeaderBuilder
from pypy.rpython.memory.gcheader import GCFLAG_TRACK_YOUNG_PTRS, GCFLAG_EXTERNAL
from pypy.rpython.memory.gcheader import GCHeaderOffset, GCData
from pypy.rpython.memory.gctransform import asmgcroot
from pypy.rpython.memory.support import AddressDict
from pypy.rpython.memory.gc import env
from pypy.rpython.
