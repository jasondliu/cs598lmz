import gc, weakref

from . import _cffi_backend
from ._cffi_backend import (
    new_handle, handle_from_ptr, handle_from_buffer,
    get_types, get_struct_cache, get_exception_cache,
    get_errno, set_errno, get_last_error, set_last_error,
    get_ffi_for_type, get_type_for_ffi,
    get_cached_btype, get_cached_btype_or_null,
    get_cached_btype_or_none, get_cached_btype_or_unknown,
    get_cached_btype_or_ffitype, get_cached_btype_or_ffitype_for_opaque,
    get_cached_btype_or_none_for_value,
    get_cached_btype_or_none_for_opaque,
    get_cached_btype_or_unknown_for_value,
    get_cached_btype_or_unknown
