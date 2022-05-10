import weakref

from . import _cffi_backend
from ._cffi_backend import (
    FFI, CDefError, VerificationError,
    new_enum_type, new_struct_type, new_union_type, new_pointer_type,
    new_function_type, new_array_type, new_void_type, new_primitive_type,
    new_raw_type, new_pointer_type, new_cdata,
    gcp, gc,
    _typeof, _sizeof, _alignmentof, _itemoffsetof, _fieldoffsetof,
    _cast, _string, _buffer, _rawdata, _rawdata_int, _rawdata_float,
    _memmove, _memset, _memcmp, _memhash,
    _get_types, _get_struct_field_types, _get_field_name, _get_field_index,
    _get_field_type, _get_field_offsetof, _get_field_sizeof,
    _get_array_length, _get_array_
