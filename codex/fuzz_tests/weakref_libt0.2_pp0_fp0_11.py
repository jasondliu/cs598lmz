import weakref

from . import _ffi
from . import _lib
from . import _util
from . import _pyutil
from . import _cdata
from . import _cffi_backend
from . import _cffi_errors
from . import _cffi_opcode
from . import _cffi_include
from . import _cffi_ext
from . import _cffi_parse
from . import _cffi_setup
from . import _cffi_test
from . import _cffi_unstub_cache

__all__ = []

# ____________________________________________________________

def _get_types(space):
    from pypy.module._cffi_backend import ctypeobj
    from pypy.module._cffi_backend import ctypeptr
    from pypy.module._cffi_backend import ctypearray
    from pypy.module._cffi_backend import ctypevoid
    from pypy.module._cffi_backend import ctypeprim
    from pypy
