import _struct

from . import _base
from . import _util
from . import _error
from . import _const

from . import _lzma_cffi

if _util.PY3:
    _long_type = int
    _int_types = (int,)
