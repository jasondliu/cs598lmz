import gc, weakref

from . import _cffi_backend
from ._cffi_backend import (
    FFI, CDefError, VerificationError,
    new_enum_type, new_struct_type, new_union_type, new_pointer_type,
    new_array_type, new_function_type, new_raw_api,
    _typeof, sizeof, alignof, buffer, cast, string,
    callback, init_once,
    _copy_struct_to_raw, _copy_raw_to_struct,
    _new_primitive_type, _get_types, _num_of_types,
    _encode_pointer, _decode_pointer,
    _encode_array, _decode_array,
    _encode_struct, _decode_struct,
    _get_enum_name, _get_enum_value,
    _get_field_name, _get_field_type, _get_field_offset,
    _get_field_sizeof, _get_field_alignment,
    _get_struct_
