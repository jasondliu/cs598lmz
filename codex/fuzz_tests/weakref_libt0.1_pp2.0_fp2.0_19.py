import weakref

from . import _cffi_backend
from ._cffi_backend import (
    new_handle, new_primitive_type, new_pointer_type, new_struct_type,
    new_union_type, new_enum_type, new_void_type, new_function_type,
    new_array_type, new_global, new_constant, new_string, new_struct_layout,
    new_union_layout, new_enum_layout, new_function, new_raw_api,
    new_type_from_handle, new_type_from_opaque_pointer,
    new_type_from_c_literal, new_type_from_c_struct, new_type_from_c_union,
    new_type_from_c_enum, new_type_from_c_function, new_type_from_c_array,
    new_type_from_c_pointer, new_type_from_c_constant, new_type_from_c_string,
    new_type_from_c_global
