import weakref

from . import _cffi_backend
from ._cffi_backend import (
    new_handle, get_handle, get_type_raw, get_exception,
    newp, from_handle,
    gcp, gc,
    )
from . import _cdata
from . import _cffi_errors
from . import _cffi_include
from . import _cffi_utils
from . import _embedding
from . import _pointer
from . import _rawffi
from . import _types
from . import _cffi_opcode
from . import _cffi_opcode as _opcode
from . import _cffi_parse
from . import _cffi_setup

_cffi_backend.init_once()

# ____________________________________________________________

_cffi_version = _cffi_backend.FFI_VERSION

_cffi_types = _types.types
_cffi_cache = _types.cache
_cffi_enum_types = _types.enum
