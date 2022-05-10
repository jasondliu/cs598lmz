import weakref

from . import _cffi_backend
from ._cffi_backend import (
    new_handle, new_primitive_type, new_pointer_type, new_struct_type,
    new_union_type, new_enum_type, new_array_type, new_void_type,
    new_function_type, new_function_type_with_keywords,
    new_raw_union_type, new_raw_struct_type,
    new_pointer_to_array_type, new_pointer_to_function_type,
    new_pointer_to_function_type_with_keywords,
    new_pointer_to_void_type, new_pointer_to_primitive_type,
    new_pointer_to_struct_type, new_pointer_to_union_type,
    new_pointer_to_enum_type, new_pointer_to_raw_struct_type,
    new_pointer_to_raw_union_type,
    new_pointer_to_pointer_type, new_pointer_to_pointer_to_
