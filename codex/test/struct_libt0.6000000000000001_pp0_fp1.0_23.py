import _struct
import _string
from array import array

from collections import namedtuple

from pypy.rlib.objectmodel import specialize
from pypy.rlib.rarithmetic import r_uint, intmask, r_ulonglong
from pypy.rpython.lltypesystem import lltype, llmemory, rclass
from pypy.rpython.lltypesystem.llmemory import weakref_create, weakref_deref
from pypy.rpython.lltypesystem.llmemory import WEAKREF, WEAKREF_TYPE
from pypy.rpython.lltypesystem.llmemory import NULL, raw_malloc_usage
from pypy.rpython.lltypesystem.rstr import string_repr
from pypy.rpython.tool import rffi_platform as platform
from pypy.rpython.lltypesystem.rstr import copy_string_to_raw
from pypy.rpython.lltypesystem.rstr import copy_raw_to_string
