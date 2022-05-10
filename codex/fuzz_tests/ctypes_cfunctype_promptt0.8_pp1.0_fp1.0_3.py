import ctypes
# Test ctypes.CFUNCTYPE
#
# This is a cffi port of the (rather old) "test_cfunctype.py" from CPython:
# https://github.com/python/cpython/blob/3.3/Lib/ctypes/test/test_cfunctype.py
#
# CPython's "test_cfunctype.py" is a regression test for ctypes,
# and that's what we are doing here. It was written in 2005/2006 by
# Thomas Heller <theller@ctypes.org> when ctypes was a Boost.Python-
# based project.

import _cffi_backend as _cffi1

from cffi import FFI
import _cffi_backend as _cffi2

assert _cffi1 is _cffi2

ffi = FFI()
C = ffi.dlopen(None)   # None is the special handle to ctypes.CDLL(None)

#
# The original test used (and ran) real C external functions.
# Here we use dummy ones:

#
