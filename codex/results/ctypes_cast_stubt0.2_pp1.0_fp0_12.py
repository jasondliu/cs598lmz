import ctypes
ctypes.cast(0, ctypes.py_object)

# SOURCE LINE 4

from rpython.rlib.objectmodel import we_are_translated
from rpython.rlib.rarithmetic import intmask
from rpython.rlib.rstring import StringBuilder
from rpython.rlib.rstruct.runpack import runpack
from rpython.rlib.rstruct.nativefmttable import native_is_bigendian
from rpython.rlib.rstruct.error import StructError
from rpython.rtyper.lltypesystem import rffi, lltype
from rpython.rtyper.tool import rffi_platform
from rpython.translator.tool.cbuild import ExternalCompilationInfo

# ____________________________________________________________

eci = ExternalCompilationInfo(
    includes = ['string.h'],
    libraries = ['m'],
    )

def external(name, args, result):
    return rffi.llexternal(name, args, result, compilation_info=eci)

memcpy = external('memcpy', [rffi
