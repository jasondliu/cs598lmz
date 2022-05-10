import weakref

from . import _cffi_backend
from ._cffi_backend import (
    FFI, CDefError, VerificationError,
    new_enum_type, new_struct_type, new_union_type, new_pointer_type,
    new_function_type, new_array_type, new_void_type,
    new_primitive_type, new_opaque_type,
    get_cached_btype,
    _typeof, _sizeof, _alignmentof,
    _get_types, _get_struct_field, _get_struct_fields,
    _get_enum_values, _get_enum_value,
    _get_field_name, _get_field_type, _get_field_offset,
    _get_array_length, _get_array_item,
    _get_function_arg_types, _get_function_result_type,
    _get_function_flags, _get_function_type,
    _get_pointer_type, _get_pointer_to_item,
   
