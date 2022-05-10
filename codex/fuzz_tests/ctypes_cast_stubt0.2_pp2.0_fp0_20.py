import ctypes
ctypes.cast(0, ctypes.py_object)

# SOURCE LINE 2

from rpython.rlib import rgc
from rpython.rlib.objectmodel import specialize, we_are_translated
from rpython.rlib.rarithmetic import intmask
from rpython.rlib.rstring import StringBuilder
from rpython.rtyper.lltypesystem import lltype, rffi
from rpython.rtyper.lltypesystem.lloperation import llop
from rpython.rtyper.lltypesystem.llmemory import raw_malloc_usage, raw_free, \
     raw_memcopy, raw_memclear, raw_malloc_usage, NULL, raw_malloc_usage, \
     raw_memmove, raw_memcopy_nonmoving
from rpython.rtyper.lltypesystem.llmemory import raw_memcopy_nonmoving
from rpython.rtyper.lltypesystem.rstr import copy_string_to_raw
from rpython.rtyper.lltypesystem.rstr import copy_string_to_raw
from rpython.r
