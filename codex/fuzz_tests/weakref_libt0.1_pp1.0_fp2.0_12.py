import weakref

from . import _cffi_backend
from ._cffi_backend import (
    _typeof, _get_types, _get_struct_layout, _get_size_and_alignment,
    _get_array_type, _get_field_name, _get_field_type, _get_field_offset,
    _get_field_index, _get_field_size, _get_field_alignment,
    _get_field_array_length, _get_field_array_item_size,
    _get_field_array_item_alignment, _get_field_array_item_type,
    _get_field_bitfield_offset, _get_field_bitfield_size,
    _get_field_bitfield_type, _get_field_bitfield_length,
    _get_field_bitfield_item_size, _get_field_bitfield_item_alignment,
    _get_field_bitfield_item_type, _get_field_bitfield_item_index,
    _get_field
