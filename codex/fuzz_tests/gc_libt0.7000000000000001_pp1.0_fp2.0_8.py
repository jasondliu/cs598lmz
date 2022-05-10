import gc, weakref

try:
    from pypy.rpython.lltypesystem.lloperation import llop
    from pypy.rpython.lltypesystem import lltype
    from pypy.rpython.rtyper.lltypesystem.rclass import (
        OBJECT, getinstancerepr, getclassrepr)
    from pypy.rpython.rtyper.lltypesystem.rclass import (
        get_type_repr, get_callable_name)
    from pypy.rpython.rtyper.lltypesystem import llmemory
    from pypy.rpython.rtyper.lltypesystem.rstr import STR, mallocstr
    from pypy.rpython.lltypesystem.lloperation import llop
    from pypy.rpython.lltypesystem.llmemory import raw_malloc_usage
    from pypy.rpython.lltypesystem.llmemory import raw_free, raw_memclear
    from pypy.rpython.lltypesystem.llmemory import itemoffsetof
    from pypy.r
