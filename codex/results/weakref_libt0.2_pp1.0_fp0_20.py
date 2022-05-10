import weakref

from . import _cffi_backend
from ._cffi_backend import (
    FFI, CDefError, VerificationError,
    new_enum_type, new_struct_type, new_union_type, new_pointer_type,
    new_function_type, new_array_type, new_void_type, new_primitive_type,
    new_opaque_type, new_handle_type,
    gcp, keepalive_key, keepalive_until_here,
    _typeof, _sizeof, _alignof, _rawaddressof, _cast, _string, _unpack_generic,
    _pack_generic, _buffer, _memmove, _memset, _memcmp, _memhash,
    _encode_pointer, _decode_pointer, _get_types, _get_field_types,
    _get_struct_layout, _get_array_type, _get_pointer_type,
    _get_function_type, _get_enum_type, _get_primitive_type,

