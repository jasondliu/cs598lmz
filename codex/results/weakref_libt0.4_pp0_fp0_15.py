import weakref

from . import _ffi
from . import _lib
from . import _util
from . import _errors
from . import _enums
from . import _types
from . import _constants
from . import _native
from . import _opcode
from . import _check
from . import _exceptions
from . import _compat
from . import _version
from . import _compat

from . import _types as types
from . import _enums as enums
from . import _constants as constants
from . import _errors as errors
from . import _native as native
from . import _opcode as opcode
from . import _check as check
from . import _exceptions as exceptions
from . import _compat as compat
from . import _version as version

from ._compat import range


def _make_error_check(error):
    def check(result, func, args):
        if result == error:
            raise errors.get_last_error()
        return result
    return check


_ffi.cdef("""
typedef void (*virFree
