import weakref

from . import _cffi_backend
from ._cffi_backend import (
    FFI, CDefError, VerificationError,
    new_enum_type, new_struct_type, new_union_type, new_pointer_type,
    new_function_type, new_raw_api,
    _typeof, _sizeof, _alignmentof, _get_types, _get_struct_field,
    _get_field_index, _get_field_name, _get_field_type, _get_field_offset,
    _get_enum_name, _get_enum_value, _get_function_addr, _get_function_type,
    _get_function_argtypes, _get_function_restype, _get_function_errno,
    _get_function_rawcall, _get_function_closure, _get_function_rawcall_trampoline,
    _get_function_closure_trampoline, _get_closure_errno, _get_closure_argtypes,
    _get_closure_rest
