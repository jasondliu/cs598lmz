import weakref

from . import _cffi_backend
from ._cffi_backend import (
    new_handle, new_enum_type, new_struct_type, new_union_type,
    new_pointer_type, new_array_type, new_function_type,
    new_global_var, new_raw_address,
    gcp, gc_clear_extra_info,
    FFIError, VerificationError,
    CDefError,
    _typeof, _get_types, _get_struct_field, _get_array_length,
    _get_field_name, _get_field_index, _get_field_type,
    _get_enum_name, _get_enum_value,
    _get_type_name, _get_type_tag, _get_type_size, _get_type_alignment,
    _get_type_kind, _get_type_elements,
    _get_function_arg_type, _get_function_arg_types,
    _get_function_result_type, _
