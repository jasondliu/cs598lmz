import gc, weakref

from . import _cffi_backend
from ._cffi_backend import (
    FFI, CDefError, VerificationError, VerificationMissing,
    new_primitive_type, new_pointer_type, new_array_type, new_struct_type,
    new_union_type, new_enum_type, new_void_type, new_function_type,
    new_raw_api, new_type_from_opaque_pointer,
    _typeof, sizeof, alignment, typeoffsetof,
    cast, addressof, byref,
    string, unpack, unpack_from, pack, pack_into,
    new, buffer, memmove, memset,
    callback,
    getctype, getcname,
    gcpolicy,
    CConstant,
    CData, CDataOwning,
    CField,
    CDataMeta,
    _CDataMeta_output,
    _CDataMeta_repr,
    _CDataMeta_str,
    _CDataMeta_getcfield,
   
