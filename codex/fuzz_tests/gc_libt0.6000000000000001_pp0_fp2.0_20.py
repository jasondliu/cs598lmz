import gc, weakref
from rpython.rtyper.lltypesystem.rstr import string_repr
from rpython.rtyper.lltypesystem.rstr import mallocstr, copystrcontent
from rpython.rtyper.lltypesystem.rstr import copyunicodecontent
from rpython.rtyper.lltypesystem.rstr import UNICODE
from rpython.rtyper.lltypesystem.rstr import STR
from rpython.rtyper.lltypesystem import lltype, rstr, rffi
from rpython.rtyper.lltypesystem.llmemory import raw_malloc_usage, raw_free_usage
from rpython.rtyper.lltypesystem.llmemory import raw_memcopy, raw_memclear
from rpython.rtyper.lltypesystem.llmemory import NULL, raw_malloc_usage
from rpython.rtyper.lltypesystem.llmemory import raw_memclear
from rpython.rtyper.lltypesystem.llmemory import raw_memcopy
from rpython.rtyper.lltypesystem.llmemory import
