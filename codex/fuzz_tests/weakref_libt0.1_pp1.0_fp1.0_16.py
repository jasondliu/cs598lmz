import weakref

from . import _cffi_backend
from ._cffi_backend import (
    FFI, CDefError, VerificationError,
    new_enum_type, new_struct_type, new_union_type, new_pointer_type,
    new_function_type, new_array_type, new_void_type, new_primitive_type,
    new_raw_pointer_type, new_opaque_type, new_handle_type,
    new_cdata, newp_cdata,
    cast, cast_pointer, cast_opaque_pointer,
    addressof, sizeof, alignof,
    callback,
    string,
    getcname,
    gcp,
    unpack_value, unpack_pointer, unpack_array, unpack_struct, unpack_union,
    unpack_enum, unpack_raw_pointer, unpack_opaque_pointer, unpack_handle,
    unpack_cdata, unpack_primitive_value, unpack_ptr_to_int,
    unpack_ptr
