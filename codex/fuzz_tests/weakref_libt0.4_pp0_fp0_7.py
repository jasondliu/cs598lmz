import weakref

from . import _lib
from . import _ffi
from . import _core
from . import _cffi_utils
from . import _cffi_backend
from . import _cffi_errors

from .cparser import ParserError

# ____________________________________________________________

_cffi_cache = {}

def _make_ffi_library(name, ffi, flags, verify, backend):
    if name in _cffi_cache:
        raise _cffi_errors.VerificationError(
            "library '%s' already loaded" % (name,))
    if not isinstance(flags, (list, tuple)):
        flags = [flags]
    if backend is None:
        backend = _cffi_backend.FFI()
    ffiobj = _FFILibrary(name, ffi, flags, verify, backend)
    _cffi_cache[name] = ffiobj
    return ffiobj

class _FFILibrary(object):
    def __init__(self, name, ffi, flags,
