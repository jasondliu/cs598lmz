import _struct
from _struct import *

import types
from types import *

import _weakref
from _weakref import *

import gc
from gc import *

# libffi types
# XXX force libffi to use ffi_type pointers internally
libffi = _ffi_backend.load("_libffi")
libffi.cast("void*", libffi.ffi_type_voidp())
libffi.cast("signed char", libffi.ffi_type_schar())
libffi.cast("unsigned char", libffi.ffi_type_uchar())
libffi.cast("signed short", libffi.ffi_type_sshort())
libffi.cast("unsigned short", libffi.ffi_type_ushort())
libffi.cast("signed int", libffi.ffi_type_sint())
libffi.cast("unsigned int", libffi.ffi_type_uint())
libffi.cast("signed long", libffi.ffi_type_slong())
