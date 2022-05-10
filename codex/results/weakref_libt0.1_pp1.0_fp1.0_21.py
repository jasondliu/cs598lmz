import weakref

from . import _cffi_backend
from ._cffi_backend import (
    FFI, CDefError, VerificationError,
    new_enum_type, new_struct_type, new_union_type, new_pointer_type,
    new_function_type, new_array_type, new_void_type, new_primitive_type,
    new_opaque_type, new_handle_type,
    _typeof, _sizeof, _alignmentof, _is_struct_type, _is_union_type,
    _is_enum_type, _is_function_type, _is_array_type, _is_pointer_type,
    _is_primitive_type, _is_void_type, _is_opaque_type, _is_handle_type,
    _get_field_name, _get_field_type, _get_field_offset, _get_field_size,
    _get_field_alignment, _get_field_bits, _get_field_bits_index,
    _get
