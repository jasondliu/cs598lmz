import ctypes
ctypes.cast(0, ctypes.py_object)

# SOURCE LINE 4

from rpython.rlib.rarithmetic import intmask
from rpython.rlib.rstring import StringBuilder
from rpython.rlib.objectmodel import specialize
from rpython.rlib.objectmodel import we_are_translated
from rpython.rlib.unroll import unrolling_iterable
from rpython.rtyper.lltypesystem import lltype, rffi
from rpython.rtyper.tool import rffi_platform
from rpython.translator.tool.cbuild import ExternalCompilationInfo
from rpython.translator.platform import platform

import sys

if sys.platform == 'win32':
    from rpython.rlib import rwin32
    from rpython.rlib.rwin32 import GetLastError, SetLastError

# ____________________________________________________________
#
#  Low-level types.

# XXX this is a mess, we should clean this up

if sys.platform == 'win32':
    _WIN32 = True
    _MS_WINDOWS = True
