import gc, weakref

from . import _cffi_backend
from ._cffi_backend import (
    FFI, CDefError, VerificationError, VerificationMissing,
    new_primitive_type, new_pointer_type, new_array_type, new_struct_type,
    new_union_type, new_enum_type, new_void_type, new_function_type,
    new_raw_api, new_type_from_opaque_pointer,
    cast, cast_pointer, cast_opaque_pointer,
    string, unpack_from, unpack_from_raw, pack_into, pack_into_raw,
    callback,
    getctype, sizeof, alignof, typeof,
    addressof, byref,
    gcp, gc_cleanup,
    _typeof, _get_types, _get_fielddescrs, _get_cached_btype,
    _backend_from_address, _backend_from_membuf,
    _backend_from_cdata, _backend_from_c
