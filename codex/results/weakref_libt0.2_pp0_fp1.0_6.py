import weakref

from . import _cffi_backend
from ._cffi_backend import (
    FFI, CDefError, VerificationError,
    new_enum_type, new_struct_type, new_union_type, new_pointer_type,
    new_array_type, new_function_type, new_void_type,
    new_primitive_type, new_opaque_type,
    get_cached_btype,
    _typeof, _sizeof, _alignmentof, _is_struct_or_union,
    _get_field_index, _get_field_name, _get_field_type,
    _get_struct_layout, _get_struct_field_offset, _get_struct_field_size,
    _get_struct_field_name, _get_struct_field_type,
    _get_struct_first_field_name, _get_struct_first_field_type,
    _get_struct_first_field_offset, _get_struct_first_field_size,
    _get_
