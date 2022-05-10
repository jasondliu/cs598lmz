import gc, weakref, sys
from contextlib import contextmanager
from weakref import WeakValueDictionary

from . import rffi
from .lltypesystem import lltype, llmemory
from .lltypesystem.lloperation import llop
from .lltypesystem.rstr import mallocstr, STR
from .lltypesystem.rstr import copystrcontent
from .lltypesystem.rstr import copystrtochar
from .lltypesystem.rstr import copycharp2str, copystr2charp
from .lltypesystem.rstr import copyunicodetochar, copychartounicode
from .lltypesystem.rstr import free_non_gc_object
from .lltypesystem.rstr import UNICODE
from .lltypesystem.rstr import mallocunicode, copyunicodecontent
from .lltypesystem.rstr import copyunicodetounicode
from .lltypesystem.rstr import unicode_empty_string, unicode_encode_utf_8
from .lltypesystem.rstr import unicode_encode_utf_16_be, unicode_encode
