import weakref

from . import _ffi as ffi
from . import _lib as lib
from . import _util as util
from . import _errors as errors
from . import _types as types
from . import _constants as constants
from . import _cdata as cdata
from . import _cdataobj as cdataobj
from . import _rawffi as rawffi
from . import _pointer as pointer
from . import _callbacks as callbacks
from . import _buffer as buffer
from . import _obj as obj
from . import _functype as functype
from . import _ctypeobj as ctypeobj
from . import _cffi_backend as cffi_backend
from . import _embedding as embedding

__all__ = []

# ____________________________________________________________

def _get_types(space):
    return space.fromcache(types.CTypesState)

