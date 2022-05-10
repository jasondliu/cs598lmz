import gc, weakref

from pypy.annotation import model as annmodel
from pypy.annotation.model import (SomeObject, SomeInteger, SomeFloat, SomeBool,
                                  SomeString, SomeChar, SomeTuple, unionof,
                                  s_ImpossibleValue, s_None)
from pypy.annotation.policy import AnnotatorPolicy
from pypy.annotation.bookkeeper import getbookkeeper
from pypy.annotation.binaryop import raise_or_catch
from pypy.rpython.error import TyperError
from pypy.rpython.lltypesystem import lltype
from pypy.rpython.lltypesystem.lltype import (Ptr, Signed, Unsigned,
    Bool, Char, Float, Void, malloc,
    gcstruct, Handlers, nullptr, ContainerType, free,
    cast_pointer, cast_ptr_to_adr,
    ptrtoint)
from pypy.rpython.lltypesystem.llmemory import NULL, raw_malloc_usage, raw_free_usage
from pypy.
