import gc, weakref

from . import _core
from ._core import _get_c_lib_handle

from . import _internal
from ._internal import _set_module

from . import _libs
from . import _types
from . import _errors
from . import _ffi
from . import _rawffi
from . import _buffer
from . import _cffi_backend
from . import _cffi_include
from . import _embedding
from . import _verifier
from . import _cdata
from . import _cdataobj
from . import _pointers
from . import _enum_type
from . import _primitive_type
from . import _array_type
from . import _struct_union_type
from . import _pointer_type
from . import _function_type
from . import _callback_type
from . import _libraries
from . import _typeslots
from . import _typeof
from . import _api
from . import _cast
from . import _cpyext
from . import _pypy_cpyext
from . import _pypy_
