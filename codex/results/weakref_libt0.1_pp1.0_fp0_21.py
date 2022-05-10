import weakref

from . import _cffi_backend
from ._cffi_backend import (
    FFI, CDefError, VerificationError,
    new_enum_type, new_struct_type, new_union_type, new_pointer_type,
    new_function_type, new_array_type, new_void_type, new_primitive_type,
    new_opaque_type, new_handle_type, new_typedef,
    add_type_to_module, add_enumeration_to_module,
    add_variable_to_module, add_raw_definition_to_module,
    add_function_to_module,
    _typeof, _sizeof, _alignof, _offsetof, _get_errno, _strlen,
    _cast, _string, _buffer, _memmove, _memset, _rawdata,
    _encode_pointer, _decode_pointer, _get_types,
    _typeoffsetof, _typealignof, _typeof_locked,
    _backendversion,
