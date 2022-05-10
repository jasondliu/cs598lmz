import weakref

from . import _cffi_backend
from ._cffi_backend import (
    FFI, CDefError, VerificationError,
    new_enum_type, new_struct_type, new_union_type, new_pointer_type,
    new_array_type, new_function_type, new_void_type, new_primitive_type,
    new_raw_pointer_type, new_opaque_type,
    get_errno, set_errno,
    _typeof, sizeof, alignof,
    cast, addressof,
    gc,
    _backendutil,
    _parse_c_type, _c_type_is_void_ptr, _c_type_is_array,
    _c_type_is_function, _c_type_is_struct_or_union,
    _c_type_is_primitive_integer, _c_type_is_primitive_float,
    _c_type_is_primitive, _c_type_is_void, _c_type_is
