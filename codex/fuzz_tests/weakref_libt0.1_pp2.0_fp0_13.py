import weakref

from . import _cffi_backend
from ._cffi_backend import (
    _typeof, _get_types, _get_c_name, _get_cached_btype, _get_cached_btype_or_none,
    _get_field_index, _get_field_name, _get_field_type, _get_array_type,
    _get_struct_layout, _get_size_and_alignment, _get_size, _get_alignment,
    _get_type_name, _get_type_name_if_enabled, _get_type_name_cached,
    _get_type_name_or_none, _get_type_name_cached_if_enabled,
    _get_type_name_cached_or_none, _get_type_name_cached_if_enabled_or_none,
    _get_type_name_unlocked, _get_type_name_unlocked_if_enabled,
    _get_type_name_unlocked_cached,
