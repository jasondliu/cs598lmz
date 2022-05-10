import gc, weakref

from . import _cffi_backend
from ._cffi_backend import (
    FFI, CDefError, VerificationError, VerificationMissing,
    new_primitive_type, new_pointer_type, new_array_type, new_struct_type,
    new_union_type, new_enum_type, new_void_type, new_function_type,
    new_raw_api, new_type_from_opaque_pointer,
    get_cached_btype, get_cached_btype_or_null,
    cast, cast_ptr_to_int, cast_int_to_ptr,
    addressof, sizeof, alignof, typeof,
    string, unpack, unpack_from, pack, pack_into,
    new, newp,
    gcp, gc_reload_possibly_moved,
    callback,
    _typeof, _encode_pointer, _decode_pointer,
    _get_types, _get_fielddescrs, _get_fielddescr,
    _
