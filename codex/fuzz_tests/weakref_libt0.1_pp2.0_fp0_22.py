import weakref

from . import _cffi_backend
from ._cffi_backend import (
    FFI, CDefError, VerificationError,
    new_enum_type, new_struct_type, new_union_type, new_pointer_type,
    new_array_type, new_function_type, new_void_type, new_primitive_type,
    new_opaque_type, new_handle_type,
    get_cached_btype, get_cached_btype_or_none,
    get_cached_ctype, get_cached_ctype_or_none,
    get_cached_type, get_cached_type_or_none,
    get_cached_types,
    get_type_name, get_type_name_or_null,
    get_type_size, get_type_alignment, get_type_kind, get_type_kind_name,
    get_type_rawsize, get_type_rawalignment,
    get_type_rawfield_at_offset, get
