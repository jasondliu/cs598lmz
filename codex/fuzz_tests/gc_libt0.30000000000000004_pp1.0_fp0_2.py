import gc, weakref

from . import _cffi_backend
from ._cffi_backend import (
    FFI, CDefError, VerificationError, VerificationMissing,
    new_primitive_type, new_pointer_type, new_array_type, new_struct_type,
    new_union_type, new_enum_type, new_void_type, new_function_type,
    new_type_from_opaque_pointer,
    _typeof, sizeof, alignof, typeoffsetof,
    cast, addressof, byref,
    string, unpack, unpack_from, pack, pack_into,
    new, gc_alloc, gc_free,
    CData, CField, CConstant,
    getcname,
    CDataOwningGC,
    _copy_ctype, _CDataMeta,
    _get_types, _get_cached_btype, _get_cached_btype_or_none,
    _backend_cache, _backend_type_cache,
    _encode_pointer
