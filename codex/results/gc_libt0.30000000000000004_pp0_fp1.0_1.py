import gc, weakref
from collections import defaultdict

from . import _cffi_backend
from ._cffi_backend import (
    FFI, CDefError, VerificationError, VerificationMissing,
    new_primitive_type, new_pointer_type, new_array_type,
    new_struct_type, new_union_type, new_enum_type,
    new_function_type, new_void_type, new_opaque_type,
    new_enum_type, new_typedef,
    add_type_to_module,
    cast, cast_ptr_to_int, cast_int_to_ptr,
    string, unpack_from, unpack_from_raw, pack, pack_raw,
    unpack, pack_into, pack_into_raw,
    callback,
    getctype, getcname,
    sizeof, alignof, typeoffsetof,
    offsetof, sizeof, alignof, typeoffsetof,
    gcp,
    _typeof, _CData, _CDataMeta, _CDataOwning,

