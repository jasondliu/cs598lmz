import gc, weakref

from . import _cffi_backend
from ._cffi_backend import (
    FFI, CDefError, VerificationError, VerificationMissing,
    new_primitive_type, new_pointer_type, new_array_type, new_struct_type,
    new_union_type, new_enum_type, new_void_type, new_function_type,
    new_raw_api, new_type_from_opaque_pointer,
    get_cached_btype, get_cached_btype_or_none,
    _typeof, _sizeof, _alignof, _typeoffsetof, _rawffi_platform,
    _backendcapi, _num_of_types, _type_to_index, _get_types,
    _get_fielddescrs, _get_fielddescr, _get_fielddescr_index,
    _get_fielddescr_index_in_unions, _get_fielddescr_name,
    _get_fielddescr_type, _get_fielddescr_
