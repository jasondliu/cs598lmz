import gc, weakref

from . import _py3compat as py3compat
from . import _exceptions as exceptions
from . import _util as util
from . import _rawffi as rawffi
from . import _ffi
from . import _cffi_backend
from . import _cffi_include

import _cffi_backend as _backend

# ____________________________________________________________

if sys.version_info < (3,):
    def _unichr(x):
        return unichr(x)
else:
    def _unichr(x):
        return chr(x)

def _get_errno():
    return _cffi_backend.get_errno()

# ____________________________________________________________

class FFIError(exceptions.FFIError):
    pass

class VerificationError(exceptions.VerificationError):
    pass

# ____________________________________________________________

_cached_bools = {}

def Bool(x):
    # x is a bool or an integer
    if x not in _c
