import weakref

from . import _cffi_backend
from ._cffi_backend import (
    FFI, CDefError, VerificationError,
    new_enum_type, new_struct_type, new_union_type, new_pointer_type,
    new_function_type, new_array_type, new_void_type, new_primitive_type,
    new_opaque_type, new_handle_type, new_cached_type,
    _typeof, _sizeof, _alignmentof, _is_struct_type, _is_union_type,
    _is_enum_type, _is_function_type, _is_pointer_type, _is_array_type,
    _is_void_type, _is_primitive_type, _is_opaque_type, _is_handle_type,
    _is_constant_array_type, _is_variable_array_type, _is_char_array_type,
    _is_char_pointer_type, _is_char_pointer_pointer_type,

