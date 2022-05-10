import gc, weakref
from ctypes import *

from pypy.rpython.lltypesystem.rffi import sizeof, offsetof
from pypy.rpython.lltypesystem.rffi import INT, SIZE_T, VOIDP, UCHAR, SHORT
from pypy.rpython.lltypesystem.rffi import ULONG, USHORT, LONG, ULONGLONG
from pypy.rpython.lltypesystem.rffi import cast, cast_pointer
from pypy.rpython.lltypesystem.rffi import get_nonmovingbuffer, get_raw_address_of
from pypy.rpython.lltypesystem.llmemory import Address
from pypy.rpython.lltypesystem.lltype import malloc, free, nullptr, GcStruct
from pypy.rpython.lltypesystem.lltype import SignedLongLong, SignedLongLongLong, Signed
from pypy.rpython.lltypesystem.lltype import UnsignedLongLong, UnsignedLongLongLong, Unsigned
from pypy.rpython.lltypesystem.
