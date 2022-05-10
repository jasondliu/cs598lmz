import gc, weakref

from . import _cffi_backend
from ._cffi_backend import (
    FFI, CDefError, VerificationError, VerificationMissing,
    new_primitive_type, new_pointer_type, new_array_type, new_struct_type,
    new_union_type, new_enum_type, new_void_type, new_function_type,
    new_raw_api, new_opaque_type,
    typeof, sizeof, alignof,
    cast, addressof, byref,
    string, unpack, unpack_from, pack, pack_into,
    CData, CArgObject, CDataOwning,
    _typeof_cache, _sizeof_cache, _alignof_cache,
    _pointer_type_cache, _array_type_cache, _struct_union_type_cache,
    _enum_type_cache, _function_type_cache,
    _ffi_callback_cache, _ffi_type_cache,
    _new_cdata, _get_cdata_type
