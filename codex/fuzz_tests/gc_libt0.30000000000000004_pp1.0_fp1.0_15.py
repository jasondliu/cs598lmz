import gc, weakref

from rpython.rlib.objectmodel import specialize
from rpython.rlib.rarithmetic import intmask
from rpython.rlib.rstring import StringBuilder
from rpython.rlib.rweaklist import RWeakListMixin
from rpython.rlib.rweakref import RWeakKeyDictionary
from rpython.rlib.rweakref import RWeakValueDictionary
from rpython.rtyper.lltypesystem import lltype, rffi
from rpython.rtyper.lltypesystem.lloperation import llop
from rpython.rtyper.lltypesystem.llmemory import (
    NULL, raw_malloc_usage, raw_memclear, raw_memcopy,
    raw_memmove, raw_free, offsetof,
    raw_malloc_usage, raw_malloc_usage_from_object,
    raw_memclear, raw_memcopy, raw_memmove,
    raw_free, raw_malloc_usage, raw_malloc_usage_from_object,
    raw_memclear, raw_memcopy, raw_mem
