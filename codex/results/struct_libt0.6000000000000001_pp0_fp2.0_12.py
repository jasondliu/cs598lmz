import _struct

from .. import _util
from .. import _types
from .._ffi import FFIEngineError, FFIEngineError
from .._ffi import _FFI
from .._ffi import NULL
from .._ffi import string_at
from .._ffi import new
from .._ffi import addressof
from .._ffi import sizeof
from .._ffi import alignof
from .._ffi import cast
from .._ffi import memmove


__all__ = [
    "FFI",
    "FFIError",
    "FFIEngineError",
    "new_allocator",
]


_type_to_ffi_type = {
    type(None): _FFI.type_void,
    bool: _FFI.type_uint,
    int: _FFI.type_sint,
    float: _FFI.type_double,
    _types.Reference: _FFI.type_pointer,
    _types.Pointer: _FFI.type_pointer,
    _types.Struct: _FFI.type_
