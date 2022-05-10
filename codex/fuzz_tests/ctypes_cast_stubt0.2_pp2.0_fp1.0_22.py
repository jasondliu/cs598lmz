import ctypes
ctypes.cast(0, ctypes.py_object)

# SOURCE LINE 4

from rpython.rlib.rarithmetic import intmask
from rpython.rlib.objectmodel import specialize, we_are_translated
from rpython.rlib.rstring import StringBuilder
from rpython.rlib.rstruct.runpack import runpack
from rpython.rlib.rstruct.nativefmttable import native_is_bigendian
from rpython.rtyper.lltypesystem import rffi, lltype
from rpython.rtyper.tool import rffi_platform
from rpython.translator.tool.cbuild import ExternalCompilationInfo
from rpython.translator.platform import platform

eci = ExternalCompilationInfo(
    includes = ['src/md5.h'],
    separate_module_sources = ['''
        #include "src/md5.h"
        #include "src/md5.c"
    '''],
    post_include_bits = ['''
        #ifndef MD5_DIGEST_SIZE
       
