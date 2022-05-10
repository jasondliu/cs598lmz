import _struct

from . import _cffi_backend
from . import _cffi_include
from . import _typeof
from . import _cdataobj


# ____________________________________________________________
#
# a few helpers

def _copy_type(TYPE):
    if isinstance(TYPE, _cffi_backend.CDataMeta):
        return TYPE
    return type(TYPE)

if _cffi_backend.get_errno is None:
    def _get_errno():
        return _cffi_backend.ffi.errno
else:
    def _get_errno():
        return _cffi_backend.get_errno()

#
# ____________________________________________________________

def _utf8(s):
    if isinstance(s, str):
        return s.encode('utf-8')
    return s

def _as_bytes(s):
    if isinstance(s, str):
        return s.encode('latin-1')
    return s
