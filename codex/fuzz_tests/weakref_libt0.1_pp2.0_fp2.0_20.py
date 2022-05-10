import weakref

from . import _cffi_backend
from ._cffi_backend import (
    FFI, CDefError, VerificationError,
    new_enum_type, new_struct_type, new_union_type, new_pointer_type,
    new_array_type, new_function_type, new_void_type, new_primitive_type,
    new_opaque_type, new_handle_type,
    get_cached_btype, get_cached_btype_or_null,
    get_cached_ctype, get_cached_ctype_or_null,
    get_cached_exception, get_cached_exception_or_null,
    get_cached_type, get_cached_type_or_null,
    get_cached_value, get_cached_value_or_null,
    get_cached_btype_or_nonnull, get_cached_ctype_or_nonnull,
    get_cached_exception_or_nonnull, get_
