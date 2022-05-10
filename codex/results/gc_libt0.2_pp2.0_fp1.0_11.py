import gc, weakref

from . import _cffi_backend
from ._cffi_backend import (
    FFI, CDefError, VerificationError,
    new_primitive_type, new_pointer_type, new_array_type,
    new_struct_type, new_union_type, new_enum_type,
    new_void_type, new_function_type,
    new_raw_api, new_type_from_opaque_pointer,
    new_type_from_cdata,
    get_cached_btype, get_cached_btype_or_none,
    _typeof, _sizeof, _alignmentof, _itemoffsetof,
    _cast, _ptradd, _rawaddressof, _typeoffsetof,
    _get_types, _get_fielddescrs, _get_fielddescr,
    _get_size_and_alignment, _get_array_length,
    _get_c_name, _get_c_name_of_type,
    _backend_type_name, _back
