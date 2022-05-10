import weakref

from . import _cffi_backend
from ._cffi_backend import (
    new_handle, new_enum_type, new_struct_type, new_union_type, new_pointer_type,
    new_array_type, new_function_type, new_void_type, new_primitive_type,
    new_opaque_type, new_constant, new_global, new_function, new_raw_api,
    new_type_from_handle, new_type_from_opaque_and_size,
    new_type_from_opaque, new_type_from_c_class, new_type_from_c_function,
    new_type_from_c_function_pointer, new_type_from_c_function_pointer_and_size,
    new_type_from_c_function_pointer_and_length, new_type_from_c_function_and_size,
    new_type_from_c_function_and_length, new_type_from_c_function_and_data,

