import weakref

from . import _cffi_backend
from ._cffi_backend import (
    new_handle, new_enum_type, new_struct_type, new_union_type, new_pointer_type,
    new_array_type, new_function_type, new_raw_union_type, new_raw_struct_type,
    new_void_type, new_primitive_type, new_opaque_type, new_constant_int,
    new_constant_float, new_constant_char, new_constant_string,
    new_constant_longdouble, new_constant_complex, new_constant_pointer,
    new_constant_struct, new_constant_union, new_constant_enum,
    new_global_var, new_global_const, new_global_const_ptr,
    new_global_const_struct, new_global_const_union, new_global_const_enum,
    new_global_const_string, new_global_const_complex,
    new_global_const
