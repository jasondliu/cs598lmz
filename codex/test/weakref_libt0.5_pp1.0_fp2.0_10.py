import weakref

from typing import Any, Dict, Optional, Union

from . import _base, _config, _utils

# Import the low-level C API.
from ._core import ffi, lib

_log = logging.getLogger(__name__)


class _ReferenceType(_base.BaseType):
    """
    Base type for all reference types.
    """

    #: The low-level CFFI type corresponding to this type.
    cffi_type = ffi.typeof("struct _cffi_backend_ctx *")

    #: The low-level CFFI type corresponding to a pointer to this type.
    cffi_pointer_type = ffi.typeof("struct _cffi_backend_ctx **")

    #: The low-level CFFI type corresponding to a pointer to this type.
    cffi_const_pointer_type = ffi.typeof("const struct _cffi_backend_ctx **")

    #: The low-level CFFI type corresponding to a pointer to this type.
    cffi
