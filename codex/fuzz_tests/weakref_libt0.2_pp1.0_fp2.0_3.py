import weakref

from . import _cffi_backend
from ._cffi_backend import (
    _get_types, _get_struct_union_class, _get_enum_class, _get_typedef,
    _get_size_and_alignment, _get_fielddescrs, _get_array_type,
    _get_pointer_type, _get_function_type, _get_void_p_type,
    _get_packed_fielddescrs, _get_raw_address, _get_raw_field_attr,
    _get_raw_struct, _get_raw_union, _get_raw_enum, _get_raw_pointer,
    _get_raw_function, _get_raw_array, _get_raw_string, _get_raw_wstring,
    _get_raw_record, _get_raw_enum_identifier, _get_raw_enum_constant,
    _get_raw_bitfield, _get_raw_bitfield_attr, _get_raw_bitfield_identifier,
    _
