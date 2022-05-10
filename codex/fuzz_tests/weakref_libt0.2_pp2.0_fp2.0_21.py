import weakref

from . import _cffi_backend
from ._cffi_backend import (
    FFI, VerificationError, CDefError,
    new_handle, from_handle,
    _typeof, _encode_pointer, _decode_pointer,
    _encode_array, _decode_array,
    _encode_struct, _decode_struct,
    _encode_union, _decode_union,
    _encode_enum, _decode_enum,
    _encode_int, _decode_int,
    _encode_char, _decode_char,
    _encode_float, _decode_float,
    _encode_double, _decode_double,
    _encode_longdouble, _decode_longdouble,
    _encode_voidp, _decode_voidp,
    _encode_size_t, _decode_size_t,
    _encode_ssize_t, _decode_ssize_t,
    _encode_ptrdiff
