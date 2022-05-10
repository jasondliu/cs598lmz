import gc, weakref
import os

from . import _cffi_backend
from ._cffi_backend import new_handle, get_handle, _typeof, FFIError

# ____________________________________________________________
#
#  A few utility functions

def _make_ffi_library(name, flags, verify_source, libraries, library_dirs,
                      runtime_library_dirs, export_symbols, ext_package):
    if not isinstance(name, str):
        raise TypeError("name must be a str, got %r" % (name,))
    if not isinstance(flags, (list, tuple)):
        raise TypeError("flags must be a list or tuple, got %r" % (flags,))
    if not isinstance(verify_source, str):
        raise TypeError("verify_source must be a str, got %r" %
                        (verify_source,))
    if not isinstance(libraries, (list, tuple)):
        raise TypeError("libraries must be a list or tuple, got %r" %
                        (libraries
