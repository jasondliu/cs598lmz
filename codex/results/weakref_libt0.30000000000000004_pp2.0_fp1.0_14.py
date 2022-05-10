import weakref
from . import _cffi_backend
from ._cffi_backend import (
    new_handle, new_enum_type, new_struct_type, new_union_type,
    new_pointer_type, new_array_type, new_function_type,
    new_raw_struct_layout, new_primitive_type, new_void_type,
    new_opaque_type, new_pointer_type, new_const_pointer_type,
    new_void_ptr_type, new_enum_type, new_typedef, new_type_pointer,
    new_type_void, new_type_primitive, new_type_struct, new_type_union,
    new_type_enum, new_type_function, new_type_array, new_type_pointer,
    new_type_const_pointer, new_type_opaque, new_type_typedef,
    new_type_void_ptr, new_type_const, new_type_volatile, new_type_pointer,
    new_type_const_
